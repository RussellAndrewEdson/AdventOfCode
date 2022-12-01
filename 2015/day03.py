#!/usr/bin/python3

# Python code for the Advent of Code 2015, Day 3.
#
# Code author: Russell A. Edson
# Date last modified: 01/12/2022

# Read in puzzle input
with open('day03.txt') as file:
    instructions = file.readline().strip()
instructions = list(instructions)

# Santa is delivering presents on a grid, and Part 1 wants us to
# keep track of which houses have been visited. We can do this
# by keeping a list of houses visited (with the (0,0) house as the
# starting point):
current_position = (0, 0)
houses = {current_position: 1}

def visit_house(position):
    """Visit the house at the current position."""
    prev_visits = houses.get(position, 0)
    houses[position] = prev_visits + 1

# Then we just parse appropriately from the given positions.
def new_position(old_position, instruction):
    """Return the new position based on the given instruction."""
    x, y = old_position
    if instruction == '<':
        x = x - 1
    elif instruction == '>':
        x = x + 1
    elif instruction == '^':
        y = y + 1
    elif instruction == 'v':
        y = y - 1
    return (x, y)

for instruction in instructions:
    current_position = new_position(current_position, instruction)
    visit_house(current_position)

# For Part 1, the number of houses that received at least one present
# is just the length of the 'houses' dictionary that was built up:
print(len(houses))

# For Part 2, Santa and Robo-Santa take turns alternating delivering
# presents, so we simply alternate current positions.
santa_position = (0, 0)
robo_position = (0, 0)
houses = {(0, 0): 2}

for index, instruction in enumerate(instructions):
    if index % 2 == 0:
        santa_position = new_position(santa_position, instruction)
        visit_house(santa_position)
    else:
        robo_position = new_position(robo_position, instruction)
        visit_house(robo_position)

# Then the number of houses that received a present is just the
# length of this dictionary again.
print(len(houses))
