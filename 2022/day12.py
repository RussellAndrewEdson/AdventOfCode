#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 12.
#
# Code author: Russell A. Edson
# Date last modified: 12/12/2022

# Read in puzzle input
with open('day12.txt') as file:
    heightmap = [list(line.strip()) for line in file]

# We want to find the path through the area that leads from the start
# 'S' to the end 'E' in the shortest amount of steps, moving only left,
# right, up or down each move, and only to levels that are at most 1
# higher than the current level. We can do this with a search
# algorithm, keeping track of moves to check in a buffer.
map_size = (len(heightmap), len(heightmap[0]))

def locate(char):
    """Return the (first) heightmap index for the given char."""
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if heightmap[i][j] == char:
                return (i, j)
    return None

start_point = locate('S')
end_point = locate('E')

def valid_move_char(current_char, next_char):
    """True if a move can be made from current_char to next_char."""
    if current_char == 'S':
        current_char = 'a'
    elif current_char == 'E':
        current_char = 'z'
    if next_char == 'S':
        next_char = 'a'
    elif next_char == 'E':
        next_char = 'z'
    return ord(next_char) - 1 <= ord(current_char)

def valid_move(current_index, next_index):
    """True if a move can be made from current_index to next_index."""
    current_height = heightmap[current_index[0]][current_index[1]]
    next_height = heightmap[next_index[0]][next_index[1]]
    return valid_move_char(current_height, next_height)

def moves_possible(index):
    """Return the indices for possible moves from the given index."""
    i, j = index
    current_char = heightmap[i][j]
    moves = []
    if i > 0:
        moves.append((i - 1, j))
    if j > 0:
        moves.append((i, j - 1))
    if i < map_size[0] - 1:
        moves.append((i + 1, j))
    if j < map_size[1] - 1:
        moves.append((i, j + 1))

    return list(filter(lambda other: valid_move(index, other), moves))

step_count = 0
steps = {start_point: step_count}
moves = moves_possible(start_point)

# Part 1 requires us to find the number of moves from the start to the
# end point 'E' with the best signal strength.
end_reached = False
while not end_reached:
    step_count = step_count + 1
    next_moves = []

    while moves:
        move = moves[0]
        moves = moves[1:]
        if heightmap[move[0]][move[1]] == 'E':
            end_reached = True
        if steps.get(move, None) is None:
            steps[move] = step_count
            next_moves = next_moves + moves_possible(move)
    moves = next_moves

# The fewest steps required from 'S' to 'E' is
print(steps[end_point])

# For Part 2, we want to find the shortest path from any 'a' height
# to the end point 'E': or identically, the shortest path from 'E'
# to a height of 'a'. We can do this using a similar algorithm as
# above, but reversing the logic: he we step down by at most one
# height per step, eminating out from the 'E' point.
def valid_move_char_part2(current_char, next_char):
    """True if a move can be made from current_char to next_char."""
    if current_char == 'S':
        current_char = 'a'
    elif current_char == 'E':
        current_char = 'z'
    if next_char == 'S':
        next_char = 'a'
    elif next_char == 'E':
        next_char = 'z'
    return ord(current_char) - 1 <= ord(next_char)

def valid_move_part2(current_index, next_index):
    """True if a move can be made from current_index to next_index."""
    current_height = heightmap[current_index[0]][current_index[1]]
    next_height = heightmap[next_index[0]][next_index[1]]
    return valid_move_char_part2(current_height, next_height)

def moves_possible_part2(index):
    """Return the indices for possible moves from the given index."""
    i, j = index
    current_char = heightmap[i][j]
    moves = []
    if i > 0:
        moves.append((i - 1, j))
    if j > 0:
        moves.append((i, j - 1))
    if i < map_size[0] - 1:
        moves.append((i + 1, j))
    if j < map_size[1] - 1:
        moves.append((i, j + 1))

    return list(filter(lambda other: valid_move_part2(index, other), moves))

step_count = 0
steps = {end_point: step_count}
moves = moves_possible_part2(end_point)

a_reached = False
a_point = None
while not a_reached:
    step_count = step_count + 1
    next_moves = []

    while moves:
        move = moves[0]
        moves = moves[1:]
        if heightmap[move[0]][move[1]] == 'a' or \
                heightmap[move[0]][move[1]] == 'S':
            a_reached = True
            a_point = move
        if steps.get(move, None) is None:
            steps[move] = step_count
            next_moves = next_moves + moves_possible_part2(move)
        if a_reached == True:
            break
    moves = next_moves

# The fewest steps required from 'E' to 'a' is
print(steps[a_point])
