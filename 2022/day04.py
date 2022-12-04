#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 4.
#
# Code author: Russell A. Edson
# Date last modified: 04/12/2022

import re

# Read in puzzle input
with open('day04.txt') as file:
    sections = [line.strip() for line in file]
sections = list(map(lambda section: re.split('-|,', section), sections))
sections = list(map(lambda pairs: list(map(int, pairs)), sections))

# Part 1 asks us to find the number of section allocations in which
# one pair is completely enclosed by the other.
def encloses(inner_section, outer_section):
    """True if the outer_section completely encloses the inner section."""
    return (inner_section[0] >= outer_section[0]) and \
           (inner_section[1] <= outer_section[1])

def containing_pair(section_pair):
    """True if the given section pair is a containing pair."""
    section1 = section_pair[0:2]
    section2 = section_pair[2:4]
    return encloses(section1, section2) or encloses(section2, section1)

print(len(list(filter(containing_pair, sections))))

# Part 2 asks for the number of section allocations that overlap
# at all.
def overlaps(section_pair):
    """True if the given section pair overlaps."""
    section1 = section_pair[0:2]
    section2 = section_pair[2:4]
    return (section1[0] <= section2[1]) and (section2[0] <= section1[1])

print(len(list(filter(overlaps, sections))))
