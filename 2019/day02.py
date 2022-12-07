#!\usr\bin\python3

# Python code for the Advent of Code 2019, Day 2.
#
# Code author: Russell A. Edson
# Date last modified: 07/12/2022

import re
import copy

# Read in puzzle input
with open('day02.txt') as file:
    intcode = re.split(',', file.readline().strip())
intcode = list(map(int, intcode))
init_intcode = copy.deepcopy(intcode)

# We build up the intcode parser:
def add(pos1, pos2, pos3):
    intcode[pos3] = intcode[pos1] + intcode[pos2]

def mul(pos1, pos2, pos3):
    intcode[pos3] = intcode[pos1] * intcode[pos2]

def parse():
    """Parse the intcode as a program."""
    halt = False
    read_pos = 0
    while not halt:
        opcode = intcode[read_pos]
        if opcode == 1:
            pos1 = intcode[read_pos + 1]
            pos2 = intcode[read_pos + 2]
            pos3 = intcode[read_pos + 3]
            add(pos1, pos2, pos3)
        elif opcode == 2:
            pos1 = intcode[read_pos + 1]
            pos2 = intcode[read_pos + 2]
            pos3 = intcode[read_pos + 3]
            mul(pos1, pos2, pos3)
        elif opcode == 99:
            halt = True
        read_pos = read_pos + 4

# Part 1 runs the intcode program, but with position 1 = 12
# and position 2 = 2.
intcode[1] = 12
intcode[2] = 2
parse()

# The value left at position 0 after the program halts is:
print(intcode[0])

# For Part 2, we reset the memory to the initial intcode state,
# and cycle positions 1 and 2 between 0 and 99 inclusive to find
# the input pair that produces 19690720 at position 0.
solution = 19690720
solution_found = False

for noun in range(100):
    for verb in range(100):
        intcode = copy.deepcopy(init_intcode)
        intcode[1] = noun
        intcode[2] = verb
        parse()

        if intcode[0] == solution:
            solution_found = True
            break
    if solution_found:
        break

print(100 * noun + verb)
