#!\usr\bin\python3

# Python code for the Advent of Code 2022, Day 3.
#
# Code author: Russell A. Edson
# Date last modified: 03/12/2022

# Read in puzzle input
rucksacks = []
with open('day03.txt') as file:
    for line in file:
        rucksack = line.strip()
        rucksack = [rucksack[0:len(rucksack)//2], rucksack[len(rucksack)//2:]]
        rucksacks.append(rucksack)

# Each rucksack has two compartments, and each compartment has
# different items (except for one item). We can find that item
# by looking at the intersection between the compartments:
def error_item(rucksack):
    """Return the item that appears in both compartments of the rucksack."""
    compartment1 = set(rucksack[0])
    compartment2 = set(rucksack[1])
    return compartment1.intersection(compartment2).pop()

# Part 1 then asks us to sum up the priorities, where the letters
# a-z have priorities 1-26, and the letters A-Z have priorities 27-52.
def priority(item):
    """Return the priority for the given item."""
    priority = None
    if item.islower():
        priority = ord(item) - ord('a') + 1
    elif item.isupper():
        priority = 26 + ord(item) - ord('A') + 1
    return priority

print(sum(map(lambda rucksack: priority(error_item(rucksack)), rucksacks)))

# For part 2, we consider the rucksacks in groups of three and
# want to find the common item between the three rucksacks (this
# is the 'badge' item type).
def badge(rucksacks):
    """Return the badge item given three rucksacks."""
    sack1, sack2, sack3 = rucksacks
    sack1 = sack1[0] + sack1[1]
    sack2 = sack2[0] + sack2[1]
    sack3 = sack3[0] + sack3[1]
    return set(sack1).intersection(set(sack2)).intersection(set(sack3)).pop()

# The priority sum for the badges is:
priority_sum = 0
for i in range(len(rucksacks)//3):
    priority_sum = priority_sum + priority(badge(rucksacks[(3*i):(3*i+3)]))
print(priority_sum)
