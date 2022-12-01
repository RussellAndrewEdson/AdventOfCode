#!/usr/bin/python3

# Python code for the Advent of Code 2015, Day 1.
#
# Code author: Russell A. Edson
# Date last modified: 01/12/2022

# Read in puzzle input
with open('day01.txt') as file:
    instructions = file.readline().strip()

# Part 1 just wants the last floor Santa arrives at, which is just
# the total of the '(' open brackets subtract the total of the ')'
# closed brackets.
instructions = list(instructions)
open_brackets = instructions.count('(')
close_brackets = instructions.count(')')

print(open_brackets - close_brackets)

# Part 2 asks for the index position of the first bracket that causes
# Santa to enter the basement (i.e. level -1). We can simply step
# along the list for this.
floor = 0
index = 0
for bracket in instructions:
    index = index + 1
    if bracket == '(':
        floor = floor + 1
    else:
        floor = floor - 1
    if floor < 0:
        break;
print(index)
