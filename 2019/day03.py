#/usr/bin/python3

# Python code for the Advent of Code 2019, Day 3.
#
# Code author: Russell A. Edson
# Date last modified: 08/12/2022

# Read in puzzle input
with open('day03.txt') as file:
    wires = [line.strip().split(',') for line in file]

# Assume the central port starts at (0,0). We want to trace
# out the two wires and determine their points of intersection.
def traverse_wire(wire):
    """Return a list of points that traces out the given wire."""
    point = [0, 0]
    wire_points = [tuple(point)]

    for movement in wire:
        direction = movement[0]
        distance = int(movement[1:])
        if direction == 'U':
            point[1] = point[1] + distance
        elif direction == 'D':
            point[1] = point[1] - distance
        elif direction == 'L':
            point[0] = point[0] - distance
        elif direction == 'R':
            point[0] = point[0] + distance
        wire_points.append(tuple(point))

    return wire_points

wires = list(map(traverse_wire, wires))
wire1, wire2 = wires

# For each consecutive pair of points (a segment) on the first wire,
# we check whether that segment intersects with any segment on the
# second wire, and if so, compute the intersection points.
def intersect_point(p1, p2, p3, p4):
    """Return the point of intersection between p1-p2 and p3-p4."""
    intersection = None

    # Determine general equations of lines connecting points
    x1, y1 = p1
    x2, y2 = p2
    a1, b1, c1 = [y2 - y1, x1 - x2, y1*x2 - x1*y2]
    x3, y3 = p3
    x4, y4 = p4
    a2, b2, c2 = [y4 - y3, x3 - x4, y3*x4 - x3*y4]

    # Intersect only if det != 0
    det = a1*b2 - a2*b1
    if det != 0:
        x = (c2*b1 - c1*b2)/det
        y = (c1*a2 - c2*a1)/det

        # Assume integer intersections for this problem, and
        # restrict to segment.
        x = int(x)
        y = int(y)
        if min(x1, x2) <= x and x <= max(x1, x2) and \
                min(x3, x4) <= x and x <= max(x3, x4) and \
                min(y1, y2) <= y and y <= max(y1, y2) and \
                min(y3, y4) <= y and y <= max(y3, y4):
            intersection = (x, y)
    return intersection

intersections = []

for index1 in range(len(wire1) - 1):
    p1, p2 = [wire1[index1], wire1[index1 + 1]]
    for index2 in range(len(wire2) - 1):
        p3, p4 = [wire2[index2], wire2[index2 + 1]]
        intersection = intersect_point(p1, p2, p3, p4)
        if intersection != None:
            intersections.append(intersection)

            if intersection[0] == 1 and intersection[1] == 0:
                print([p1, p2, p3, p4])

# Part 1 simply wants the nearest intersection to the central port,
# using the Manhattan metric.
def manhattan_dist(point1, point2):
    """Returns the Manhattan metric distance between the two points."""
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

print(min(map(lambda point: manhattan_dist((0, 0), point), intersections)))

# For Part 2, we need to determine the closest intersection along the
# wires (i.e. the one that is reached in the smallest combined number of
# steps along each wire).
def point_on_segment(p1, p2, point_to_check):
    """True if the point to check appears on p1-p2."""
    x, y = point_to_check
    x1, y1 = p1
    x2, y2 = p2

    return min(x1, x2) <= x and x <= max(x1, x2) and \
        min(y1, y2) <= y and y <= max(y1, y2)

def dist_along_wire(wire, point):
    """The distance along the wire to the given point."""
    dist = 0
    for index in range(len(wire) - 1):
        p1, p2 = [wire[index], wire[index + 1]]
        if point_on_segment(p1, p2, point):
            dist = dist + manhattan_dist(p1, point)
            break
        else:
            dist = dist + manhattan_dist(p1, p2)
    return dist

def combined_dist(point):
    """The combined distance to this point along both wires."""
    return dist_along_wire(wire1, point) + dist_along_wire(wire2, point)

print(min(map(combined_dist, intersections)))
