#!\usr\bin\python3

# Python code for the Advent of Code 2022, Day 8.
#
# Code author: Russell A. Edson
# Date last modified: 08/12/2022


# Read in puzzle input
with open('day08.txt') as file:
    grid = [list(map(int, list(line.strip()))) for line in file]
grid_size = [len(grid), len(grid[0])]


# We are given that a tree is visible from a given edge of the
# grid if all of the trees between it and the edge are shorter
# than it.
def visible(i, j, edge):
    """True if the tree at (i,j) is visible from edge (l/r/t/b)."""
    tree_height = grid[i][j]
    tree_visible = True

    if edge == 'l':
        traverse = (0, -1)
    elif edge == 'r':
        traverse = (0, 1)
    elif edge == 't':
        traverse = (-1, 0)
    else:
        traverse = (1, 0)
    i = i + traverse[0]
    j = j + traverse[1]

    while 0 <= i and i < grid_size[0] and 0 <= j and j < grid_size[1]:
        if grid[i][j] >= tree_height:
            tree_visible = False
            break
        i = i + traverse[0]
        j = j + traverse[1]

    return tree_visible

def visible_from_outside(i, j):
    """True if the tree at (i,j) is visible from at least one edge."""
    return visible(i, j, 'l') or visible(i, j, 'r') or \
        visible(i, j, 't') or visible(i, j, 'b')

# Part 1 asks for the number of trees in the grid that are visible
# from the outside.
visible_trees = 0
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        if visible_from_outside(i, j):
            visible_trees = visible_trees + 1
            
print(visible_trees)

# For Part 2, we want to determine the viewing distance for a
# tree(house) at a given index.
def viewing_distance(i, j, edge):
    """Return the viewing distance for tree (i,j) looking out to edge."""
    tree_height = grid[i][j]
    distance = 0

    if edge == 'l':
        traverse = (0, -1)
    elif edge == 'r':
        traverse = (0, 1)
    elif edge == 't':
        traverse = (-1, 0)
    else:
        traverse = (1, 0)

    i = i + traverse[0]
    j = j + traverse[1]
    while 0 <= i and i < grid_size[0] and 0 <= j and j < grid_size[1]:
        if grid[i][j] <= tree_height:
            distance = distance + 1
        if grid[i][j] >= tree_height:
            break
        i = i + traverse[0]
        j = j + traverse[1]

    return distance

def scenic_score(i, j):
    """Return the viewing distance scenic score for the tree (i,j)."""
    return viewing_distance(i, j, 'l') * viewing_distance(i, j, 'r') * \
        viewing_distance(i, j, 't') * viewing_distance(i, j, 'b')

# Part 2 asks for the maximum scenic score.
scores = []
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        scores.append(scenic_score(i, j))
print(max(scores))
