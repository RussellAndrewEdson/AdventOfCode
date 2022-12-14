#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 14.
#
# Code author: Russell A. Edson
# Date last modified: 14/12/2022

# Read in puzzle input
with open('day14.txt') as file:
    paths = [line.strip() for line in file]

# We set up the grid for the cave by parsing the paths from input
def parse_path(path):
    """Return all coordinates on a given path."""
    path = path.split(' -> ')
    junctures = list(map(lambda p: list(map(int, p.split(','))), path))

    coordinates = []
    coordinates.append(junctures[0])
    for index in range(len(junctures) - 1):
        juncture1, juncture2 = junctures[index:(index + 2)]

        # Assume only moving in 4 possible directions
        if juncture1[0] < juncture2[0]:
            for i in range(1, juncture2[0] - juncture1[0] + 1):
                coordinates.append([juncture1[0] + i, juncture1[1]])
        elif juncture1[0] > juncture2[0]:
            for i in range(1, juncture1[0] - juncture2[0] + 1):
                coordinates.append([juncture1[0] - i, juncture1[1]])
        elif juncture1[1] < juncture2[1]:
            for i in range(1, juncture2[1] - juncture1[1] + 1):
                coordinates.append([juncture1[0], juncture1[1] + i])
        elif juncture1[1] > juncture2[1]:
            for i in range(1, juncture1[1] - juncture2[1] + 1):
                coordinates.append([juncture1[0], juncture1[1] - i])
    return coordinates

paths = list(map(parse_path, paths))

minx, maxx, miny, maxy = paths[0][0] + paths[0][0]
for path in paths:
    for coordinates in path:
        if coordinates[0] < minx:
            minx = coordinates[0]
        if coordinates[0] > maxx:
            maxx = coordinates[0]
        if coordinates[1] < miny:
            miny = coordinates[1]
        if coordinates[1] > maxy:
            maxy = coordinates[1]

# We represent the grid as a set of coordinate pairs containing rocks
# (and later, another set of coordinates for sand), rather than
# hard-coding anything up in a 2D array.
rock = set()
for path in paths:
    for coordinates in path:
        rock.add(tuple(coordinates))

# Sand is produced one unit at a time from source (500, 0)
sand_source = (500, 0)
sand = set()

def sand_fall():
    """Return the next location of the falling sand for the current config."""
    grain = list(sand_source)
    stopped = False

    while not stopped:
        if grain[1] >= maxy:
            stopped = True
            break
        candidate = [grain[0], grain[1] + 1]
        t_candidate = tuple(candidate)
        if not t_candidate in rock and not t_candidate in sand:
            grain = candidate
            continue
        else:
            candidate[0] = candidate[0] - 1
            t_candidate = tuple(candidate)
            if not t_candidate in rock and not t_candidate in sand:
                grain = candidate
                continue
            else:
                candidate[0] = candidate[0] + 2
                t_candidate = tuple(candidate)
                if not t_candidate in rock and not t_candidate in sand:
                    grain = candidate
                    continue
                else:
                    stopped = True
                    break
    return tuple(grain)

# Part 1 asks us for the number of units of sand before one leaves the
# grid extent.
next_sand = sand_fall()
while next_sand[1] < maxy:
    sand.add(next_sand)
    next_sand = sand_fall()
print(len(sand))

# For Part 2, we assume that there is an infinite line of rock at
# y = maxy + 2. We simulate sand falling until the next unit of
# sand blocks the source entirely.
sand = set()

def in_rock(coordinates):
    """True if the given coordinates are in the rock set."""
    return coordinates in rock or coordinates[1] == (maxy + 2)

def sand_fall_part2():
    """Return the next location of the falling sand, for Part 2."""
    grain = list(sand_source)
    stopped = False

    while not stopped:
        candidate = [grain[0], grain[1] + 1]
        t_candidate = tuple(candidate)
        if not in_rock(t_candidate) and not t_candidate in sand:
            grain = candidate
            continue
        else:
            candidate[0] = candidate[0] - 1
            t_candidate = tuple(candidate)
            if not in_rock(t_candidate) and not t_candidate in sand:
                grain = candidate
                continue
            else:
                candidate[0] = candidate[0] + 2
                t_candidate = tuple(candidate)
                if not in_rock(t_candidate) and not t_candidate in sand:
                    grain = candidate
                    continue
                else:
                    stopped = True
                    break
    return tuple(grain)

next_sand = sand_fall_part2()
while next_sand != sand_source:
    sand.add(next_sand)
    next_sand = sand_fall_part2()
print(len(sand) + 1)
