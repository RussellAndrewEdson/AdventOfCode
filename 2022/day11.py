#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 11.
#
# Code author: Russell A. Edson
# Date last modified: 11/12/2022

import re
import operator
import copy
from functools import reduce

# Read in puzzle input
with open('day11.txt') as file:
    monkey_notes = []
    input_line = file.readline()
    while input_line:
        this_monkey = []
        while input_line and input_line != '\n':
            this_monkey.append(input_line.rstrip())
            input_line = file.readline()
        monkey_notes.append(this_monkey)
        input_line = file.readline()

# We represent each monkey as an Object
class Monkey:
    """A Monkey Object."""

    def __init__(self, notes):
        """Make a new Monkey based on the given notes."""
        self.num = int(re.search(r'(?<=Monkey )\d+(?=:)', notes[0])[0])
        self.items = list(map(int, re.findall(r'(\d+)', notes[1])))
        self.start_items = copy.deepcopy(self.items)
        self.operation = lambda old: eval(notes[2].split('= ')[1])
        self.test_divisor = int(re.search(r'\d+', notes[3])[0])
        self.throw_when_True = int(re.search(r'\d+', notes[4])[0])
        self.throw_when_False = int(re.search(r'\d+', notes[5])[0])

        # Keep track of item inspections
        self.inspection_count = 0

monkeys = [Monkey(notes) for notes in monkey_notes]

# The monkeys take turns inspecting all of their items and throwing
# them around.
def do_round():
    """Run a single round of the monkey shenanigans."""
    for monkey in monkeys:
        for item_index in range(len(monkey.items)):
            # Inspect (and div by 3 for no damage)
            item = monkey.items[0]
            monkey.items = monkey.items[1:]
            monkey.inspection_count = monkey.inspection_count + 1
            item = monkey.operation(item) // 3

            # Throw item to another monkey
            if item % monkey.test_divisor == 0:
                monkeys[monkey.throw_when_True].items.append(item)
            else:
                monkeys[monkey.throw_when_False].items.append(item)

# Part 1 asks for the product of the number of inspections from
# the two most active monkeys after 20 rounds.
for round in range(20):
    do_round()

inspections = list(map(lambda monkey: monkey.inspection_count, monkeys))
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])

# For Part 2, we no longer divide by 3 in the rounds, which means the
# item 'worry levels' can grow unbounded. However, observe that the
# item worry levels are only really used for the divisors across all of
# the monkeys, so we can simplify things by keeping track of the
# total divisor for the modulo throughout the rounds.
monkey_divisors = list(map(lambda monkey: monkey.test_divisor, monkeys))
total_divisor = reduce(operator.mul, monkey_divisors)

for monkey in monkeys:
    monkey.items = monkey.start_items
    monkey.inspection_count = 0

def do_round_part2():
    """Run a single round of the monkey shenanigans, part 2."""
    for monkey in monkeys:
        for item_index in range(len(monkey.items)):
            # Inspect
            item = monkey.items[0]
            monkey.items = monkey.items[1:]
            monkey.inspection_count = monkey.inspection_count + 1
            item = monkey.operation(item) % total_divisor

            # Throw item to another monkey
            if item % monkey.test_divisor == 0:
                monkeys[monkey.throw_when_True].items.append(item)
            else:
                monkeys[monkey.throw_when_False].items.append(item)

# The level of 'monkey business' after 10000 rounds is thus:
for round in range(10000):
    do_round_part2()

inspections = list(map(lambda monkey: monkey.inspection_count, monkeys))
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
