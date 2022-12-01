#!/usr/bin/python3

# Python code for the Advent of Code 2015, Day 5.
#
# Code author: Russell A. Edson
# Date last modified: 01/12/2022

import re

# Read in puzzle input
with open('day05.txt') as file:
    strings = [line.strip() for line in file]

# We check for 'nice' strings by checking the following properties:
def at_least_three_vowels(string):
    """True if the string has at least three vowels."""
    vowels = re.findall(r'[aeiou]', string)
    return len(vowels) >= 3

def at_least_one_double_letter(string):
    """True if the string has at least one double-letter (e.g. 'aa')."""
    return re.search(r'(.)\1', string) != None

def excludes_bad_substrings(string):
    """True if the string does not contain 'ab', 'cd', 'pq', 'xy'."""
    return re.search(r'ab|cd|pq|xy', string) == None

def nice_string(string):
    """True if the given string is a nice string."""
    return at_least_three_vowels(string) and \
        at_least_one_double_letter(string) and \
        excludes_bad_substrings(string)

# Part 1 wants the total number of nice strings.
nice_strings = list(filter(nice_string, strings))
print(len(nice_strings))

# Part 2 modifies the rules for what a nice string is:
def at_least_one_repeating_pair(string):
    """True if the string has a repeating pair (non-overlapping)."""
    return re.search(r'(.{2}).*\1', string) != None

def at_least_one_repeating_letter_separated(string):
    """True if the string has a repeated letter separated by one letter."""
    return re.search(r'(.).\1', string) != None

def nice_string_v2(string):
    """(NEW) True if the given string is a nice string."""
    return at_least_one_repeating_pair(string) and \
        at_least_one_repeating_letter_separated(string)

nice_strings = list(filter(nice_string_v2, strings))
print(len(nice_strings))
