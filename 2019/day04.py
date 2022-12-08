#!/usr/bin/python3

# Python code for the Advent of Code 2019, Day 4.
#
# Code author: Russell A. Edson
# Date last modified: 08/12/2022

import re

# Read in puzzle input
with open('day04.txt') as file:
    password_range = list(map(int, file.readline().strip().split('-')))

# Part 1 requires us to generate candidates for the password, given:
#   1. It is six-digits long and within the range provided as input,
#   2. At least 2 adjacent digits are always the same,
#   3. Digits never decrease from left-to-right.
# Brute force is sufficient here.

def adjacent_digits_same(num):
    """True if num contains at least two adjacent digits that are the same."""
    return re.search(r'(.)\1', str(num)) != None

def digits_never_decrease(num):
    """True if num's digits never decrease from left-to-right."""
    num = list(map(int, list(str(num))))
    decrease = False
    x = num[0]
    index = 1
    while not decrease and index < len(num):
        if x > num[index]:
            decrease = True
        x = num[index]
        index = index + 1
    return not(decrease)

passwords = []
for candidate in range(password_range[0], password_range[1] + 1):
    if adjacent_digits_same(candidate) and digits_never_decrease(candidate):
        passwords.append(candidate)

print(len(passwords))

# For Part 2, the rule about adjacent digits being the same is modified
# slightly:
#   2. The two adjacent digits are not part of a larger group of adjacent
#      digits (e.g. 11 is fine, 111 and 1111 don't count).

def adjacent_two_digits_same(num):
    """True if num contains exactly two adjacent digits that are the same."""
    matches = [match.group(0) for match in re.finditer(r'(.)\1+', str(num))]
    return any(map(lambda match: len(list(match)) == 2, matches))

passwords = []
for candidate in range(password_range[0], password_range[1] + 1):
    if adjacent_two_digits_same(candidate) and \
            digits_never_decrease(candidate):
        passwords.append(candidate)

print(len(passwords))
