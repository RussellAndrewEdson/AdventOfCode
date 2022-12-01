#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 1.
#
# Code author: Russell A. Edson
# Date last modified: 01/12/2022

# Read in puzzle input
with open('day01.txt') as file:
    calories_list = [line.strip() for line in file]

# Total up the calories carried by each elf
calories_totals = []
calories = 0
for line in calories_list:
    if len(line) > 0:
        calories = calories + int(line)
    else:
        calories_totals.append(calories)
        calories = 0
calories_totals.append(calories)

# Part 1 wants the elf with the most calories.
# The elf with the most calories is:
print(max(calories_totals))

# Part 2 wants the three elves with the top three most calories.
# The sum of these is:
calories_totals.sort(reverse=True)
print(sum(calories_totals[0:3]))
