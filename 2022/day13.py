#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 13.
#
# Code author: Russell A. Edson
# Date last modified: 13/12/2022

from functools import cmp_to_key
from copy import deepcopy

# Read in puzzle input:
with open('day13.txt') as file:
    packet_pairs = []
    line = True
    while line:
        line = file.readline()
        pair = [line.strip()]
        line = file.readline()
        pair.append(line.strip())
        packet_pairs.append(pair)

        # Blank line
        line = file.readline()

def parse_list(list_str):
    """Recursively return a proper list form for the given string list."""
    # Clunky but works
    list_rep = []
    items = []
    nesting_level = 0
    end_item = False
    item = []
    for char in list(list_str[1:-1]):
        if char == '[':
            nesting_level = nesting_level + 1
            item.append(char)
        elif char == ']':
            nesting_level = nesting_level - 1
            item.append(char)
            if nesting_level == 0:
                end_item = True
        elif char == ',' and nesting_level == 0:
            if len(item) > 0:
                end_item = True
        else:
            item.append(char)

        if end_item:
            items.append(''.join(item))
            item = []
            end_item = False
    if len(item) > 0:
        items.append(''.join(item))

    for item in items:
        if item[0] == '[' and item[-1] == ']':
            list_rep.append(parse_list(item))
        else:
            list_rep.append(int(item))
    return list_rep

def parse_packet_pair(packet_pair_str):
    """Return a properly-parsed pair of packets."""
    return list(map(parse_list, packet_pair_str))

packet_pairs = list(map(parse_packet_pair, packet_pairs))

# For Part 1, we need to compare packets across the pairs to determine
# which are in the right order.
def right_order(packet_pair):
    """True if the given packets are in the right order."""
    left, right = deepcopy(packet_pair)
    max_items = max(len(left), len(right))

    i = 0
    while i < max_items:
        if i >= len(left):
            return True
        elif i >= len(right):
            return False
        elif type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
            else:
                i = i + 1
        elif type(left[i]) == list and type(right[i]) == list:
            if len(left[i]) == 0:
                return True
            elif len(right[i]) == 0:
                return False
            else:
                sublist = right_order([left[i], right[i]])
                if sublist == True:
                    return True
                elif sublist == False:
                    return False
                else:
                    i = i + 1
        else:
            if type(left[i]) == int:
                left[i] = [left[i]]
            else:
                right[i] = [right[i]]

    # If we got here: indeterminate.
    return None

# The sum of the indices of the pairs that are in the right order is
indices_sum = 0
for index, pair in enumerate(packet_pairs):
    if right_order(pair):
        indices_sum = indices_sum + (index + 1)
print(indices_sum)

# For Part 2, we need to add two divider packets and sort all of the
# packets into the right order. We can do this easily using a
# custom comparator function for the sort() method.
packets = [[[2]], [[6]]]
for packet_pair in packet_pairs:
    packets.append(packet_pair[0])
    packets.append(packet_pair[1])

def compare_packets(packet1, packet2):
    """Wraps right_order() for use with the sort() function."""
    order = right_order([packet1, packet2])
    if order == True:
        return -1
    elif order == False:
        return 1
    else:
        return 0

packets.sort(key=cmp_to_key(compare_packets))

# We then find the divider packet indices and multiply them together
# to get the decoder key.
divider1 = packets.index([[2]]) + 1
divider2 = packets.index([[6]]) + 1
print(divider1 * divider2)
