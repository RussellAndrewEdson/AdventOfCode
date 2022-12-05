#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 5.
#
# Code author: Russell A. Edson
# Date last modified: 05/12/2022

import re
import copy

# Read in puzzle input
with open('day05.txt') as file:
    initial_stacks = []
    input_line = file.readline()
    while input_line != '\n':
        initial_stacks.append(input_line.rstrip())
        input_line = file.readline()

    instructions = []
    input_line = file.readline()
    while input_line:
        instructions.append(input_line.strip())
        input_line = file.readline()


# We represent the stacks as stacks (natch!), so we need to determine
# the initial configuration from the given input.

# The last line of initial_stacks contains the different stack labels:
stack_labels = re.split('\s+', initial_stacks[-1].strip())
stacks = {}
for label in stack_labels:
    stacks[label] = []

# We then loop up through the stacks in the initial configuration,
# adding the crates from bottom-to-top.
initial_stacks.pop()
while initial_stacks:
    level = initial_stacks.pop()
    for index in range(len(level)//4 + 1):
        part = level[(index*4):(4*(index + 1))].strip()
        if part != '':
            stacks[stack_labels[index]].append(part[1:2])
initial_stacks = copy.deepcopy(stacks)

# With the initial stack configuration captured, now we simply
# define a way to parse the instructions.
def run_instruction(instruction):
    """Run the given instruction on the stacks."""
    move_number, from_stack, to_stack = re.findall('\d+', instruction)
    for move in range(int(move_number)):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)

for instruction in instructions:
    run_instruction(instruction)

# For Part 1, we want the topmost crate on each stack.
topmost = list(map(lambda stack: stack[-1], stacks.values()))
print(''.join(topmost))

# For Part 2, we move multiple crates in the same order, so we need
# to reset the configuration and redefine the instruction parsing.
part1_stacks = stacks
stacks = copy.deepcopy(initial_stacks)

def run_instruction2(instruction):
    """Run the given instruction on the stacks, but for Part 2."""
    move_number, from_stack, to_stack = re.findall('\d+', instruction)
    to_be_moved = []
    for move in range(int(move_number)):
        crate = stacks[from_stack].pop()
        to_be_moved.insert(0, crate)
    stacks[to_stack] = stacks[to_stack] + to_be_moved

for instruction in instructions:
    run_instruction2(instruction)

# The topmost stacks are now:
topmost = list(map(lambda stack: stack[-1], stacks.values()))
print(''.join(topmost))
