#!/usr/bin/python3

# Python code for the Advent of Code 2019, Day 1.
#
# Code author: Russell A. Edson
# Date last modified: 07/12/2022


# Read in puzzle input
with open('day01.txt') as file:
    masses = [int(line.strip()) for line in file]

# The fuel is calculated by floor(mass/3) - 2.
def fuel(mass):
    """Return the fuel for the module, given its mass."""
    return mass // 3 - 2

# Part 1 asks for the sum of the fuels.
print(sum(list(map(fuel, masses))))

# For Part 2, we iteratively compute the fuel for the fuel masses
# too (with negative fuels being treated as zero).
def total_fuel(mass):
    """Return the total fuel (including the fuel for the fuel)."""
    accumulated_fuel = 0
    while mass > 0:
        fuel = max(0, mass // 3 - 2)
        accumulated_fuel = accumulated_fuel + fuel
        mass = fuel
    return accumulated_fuel

print(sum(list(map(total_fuel, masses))))
