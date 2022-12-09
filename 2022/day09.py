#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 9.
#
# Code author: Russell A. Edson
# Date last modified: 09/12/2022

# Read in puzzle input
with open('day09.txt') as file:
    motions = [line.strip().split(' ') for line in file]

# We represent the head and tail of the rope as coordinates
# on a 2D grid (assumed to start at [0,0] with the head covering
# the tail)
head = [0, 0]
tail = [0, 0]

# The position of the tail updates if ever the head is more than
# a single motion away (and since we move one step at a time, we only
# need to check at most 24 different positions).
def update_tail():
    """Updates the tail, returning True if the tail has moved."""
    distance = [head[0] - tail[0], head[1] - tail[1]]
    if abs(distance[0]) <= 1 and abs(distance[1]) <= 1:
        # Done: don't need to update
        return False
    elif distance[0] == 2:
        if distance[1] == 0:
            tail[0] = tail[0] + 1
        elif distance[1] > 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] + 1
        elif distance[1] < 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] - 1
    elif distance[0] == -2:
        if distance[1] == 0:
            tail[0] = tail[0] - 1
        elif distance[1] > 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] + 1
        elif distance[1] < 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] - 1
    elif distance[1] == 2:
        if distance[0] == 0:
            tail[1] = tail[1] + 1
        elif distance[0] > 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] + 1
        elif distance[0] < 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] + 1
    elif distance[1] == -2:
        if distance[0] == 0:
            tail[1] = tail[1] - 1
        elif distance[0] > 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] - 1
        elif distance[0] < 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] - 1
    return True

# Part 1 asks us to count up the number of positions that the
# tail visited at least once, which we can do with a dictionary:
positions_visited = {}

def count_position(position):
    """Count the given position as having been visited (again)."""
    position = tuple(position)
    positions_visited[position] = positions_visited.get(position, 0) + 1

count_position(tail)

def do_motion(motion):
    """Move the head according to the given motion instruction."""
    global head, tail

    movement = [0, 0]
    if motion[0] == 'L':
        movement[0] = -1
    elif motion[0] == 'R':
        movement[0] = 1
    elif motion[0] == 'U':
        movement[1] = 1
    elif motion[0] == 'D':
        movement[1] = -1

    for move in range(int(motion[1])):
        head = [head[0] + movement[0], head[1] + movement[1]]
        moved = update_tail()
        if moved:
            count_position(tail)

for motion in motions:
    do_motion(motion)

print(len(positions_visited))

# For Part 2, we now have ten knots (so ten 'tails' that follow
# the head). We can generalise the above code to update a series
# of tails in a list.
rope = []
for knot in range(10):
    rope.append([0, 0])

def update_knot(head, tail):
    """Updates the tail knot, returning True if that knot has moved."""
    distance = [head[0] - tail[0], head[1] - tail[1]]
    if abs(distance[0]) <= 1 and abs(distance[1]) <= 1:
        # Done: don't need to update
        return False
    elif distance[0] == 2:
        if distance[1] == 0:
            tail[0] = tail[0] + 1
        elif distance[1] > 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] + 1
        elif distance[1] < 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] - 1
    elif distance[0] == -2:
        if distance[1] == 0:
            tail[0] = tail[0] - 1
        elif distance[1] > 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] + 1
        elif distance[1] < 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] - 1
    elif distance[1] == 2:
        if distance[0] == 0:
            tail[1] = tail[1] + 1
        elif distance[0] > 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] + 1
        elif distance[0] < 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] + 1
    elif distance[1] == -2:
        if distance[0] == 0:
            tail[1] = tail[1] - 1
        elif distance[0] > 0:
            tail[0] = tail[0] + 1
            tail[1] = tail[1] - 1
        elif distance[0] < 0:
            tail[0] = tail[0] - 1
            tail[1] = tail[1] - 1
    return True

positions_visited = {}
count_position(rope[-1])

def do_motion_part2(motion):
    """Move the head according to the given motion instruction."""
    global rope

    movement = [0, 0]
    if motion[0] == 'L':
        movement[0] = -1
    elif motion[0] == 'R':
        movement[0] = 1
    elif motion[0] == 'U':
        movement[1] = 1
    elif motion[0] == 'D':
        movement[1] = -1

    for move in range(int(motion[1])):
        rope[0] = [rope[0][0] + movement[0], rope[0][1] + movement[1]]
        for knot in range(1, len(rope)):
            moved = update_knot(rope[knot-1], rope[knot])
        if moved:
            count_position(rope[-1])

for motion in motions:
    do_motion_part2(motion)

# The positions visited by the last knot in the rope are:
print(len(positions_visited))
