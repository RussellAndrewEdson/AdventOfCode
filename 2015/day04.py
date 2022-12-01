#!/usr/bin/python3

# Python code for the Advent of Code 2015, Day 4.
#
# Code author: Russell A. Edson
# Date last modified: 01/12/2022

import re
from hashlib import md5

# Read in puzzle input
with open('day04.txt') as file:
    secret_key = file.readline().strip()

# We combine the secret key with an integer and generate an MD5 hash:
def md5_hash(key, integer):
    """Return the md5 hash of the combined key+integer."""
    return md5((key + str(integer)).encode('utf-8')).hexdigest()

# For Part 1, we can loop to find the integer that combines with
# the given secret key to produce a hash with at least five prefix 0s:
def leading_zeros(hash):
    """Return the number of leading zeros in the hash."""
    return len(re.match(r'^[0]*', hash)[0])

integer = 1
while leading_zeros(md5_hash(secret_key, integer)) < 5:
    integer = integer + 1
print(integer)

# For Part 2, we want a hash with at least six zeros.
# (This didn't end up taking too long.)
integer = 1
while leading_zeros(md5_hash(secret_key, integer)) < 6:
    integer = integer + 1
print(integer)
