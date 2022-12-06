#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 6.
#
# Code author: Russell A. Edson
# Date last modified: 06/12/2022

import re

# Read in puzzle input
with open('day06.txt') as file:
    datastream = file.readline().strip()

# For Part 1, we need to determine the location of the
# start-of-packet marker in the datastream, which is
# the first set of 4 consecutive letters that all differ.
def common_letters(buffer):
    """True if the given buffer contains a repeating letter."""
    return re.search(r'(.).*\1', buffer) != None

def start_of_packet(buffer):
    """Return the first start-of-packet position for the given buffer."""
    position = 4
    set4 = buffer[0:4]
    buffer = list(buffer[4:])
    buffer.reverse()

    while common_letters(set4) and len(buffer) > 0:
        position = position + 1
        set4 = set4[1:] + buffer.pop()
    return position

# The first start-of-packet marker is detected in the input at:
print(start_of_packet(datastream))

# For Part 2, we look for start-of-message markers, which
# consist of 14 distinct consecutive characters.
def start_of_message(buffer):
    """Return the first start-of-message position for the given buffer."""
    position = 14
    set14 = buffer[0:14]
    buffer = list(buffer[14:])
    buffer.reverse()

    while common_letters(set14) and len(buffer) > 0:
        position = position + 1
        set14 = set14[1:] + buffer.pop()
    return position

# The first start-of-message marker is at:
print(start_of_message(datastream))
