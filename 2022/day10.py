#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 10.
#
# Code author: Russell A. Edson
# Date last modified: 10/12/2022

# Read in puzzle input
with open('day10.txt') as file:
    program = [line.strip() for line in file]

# The given input are instructions to update the x register
# in the CPU. We want to keep track of the value of x at
# each cycle:
cycles = [1]
x = 1

def noop():
    """Execute the 'noop' instruction."""
    global x
    cycles.append(x)

def addx(val):
    """Execute the 'addx val' instruction (takes two cycles)."""
    global x
    cycles.append(x)
    cycles.append(x)
    x = x + val

for instruction in program:
    if instruction == 'noop':
        noop()
    elif instruction.startswith('addx'):
        addx(int(instruction.split(' ')[1]))

# Part 1 asks for the sum of the signal strengths at the 20th, 60th,
# 100th, 140th, 180th and 220th cycles, where the signal strength is
# simply the number of the cycle multiplied by the value of the x
# register at that instant.
def signal_strength(cycle_num):
    """Return the signal strength at the given cycle_num."""
    return cycle_num * cycles[cycle_num]

signal = map(signal_strength, [20, 60, 100, 140, 180, 220])
print(sum(signal))

# For Part 2, we are given that x is the middle-position for a 3-pixel
# wide sprite being drawn on a 40px x 6px CRT. The pixels are drawn
# left to right, and if a pixel is being drawn where the sprite currently
# overlaps, then that counts as a lit pixel (the rest are dark pixels).
# (Note that the sprite only moves between 0 and 40.)
cycles = cycles[1:]
pixels = ['.']*len(cycles)
for index in range(len(cycles)):
    sprite_middle = cycles[index]
    if index % 40 in [sprite_middle - 1, sprite_middle, sprite_middle + 1]:
        pixels[index] = '#'

# Then we simply print the appropriately-formatted list.
for index in range(6):
    print(''.join(pixels[index*40:(index*40+40)]))

# The output is:

#     ###..####.####.####.#..#.###..####..##..
#     #..#.#.......#.#....#.#..#..#.#....#..#.
#     #..#.###....#..###..##...###..###..#..#.
#     ###..#.....#...#....#.#..#..#.#....####.
#     #.#..#....#....#....#.#..#..#.#....#..#.
#     #..#.#....####.####.#..#.###..#....#..#.
