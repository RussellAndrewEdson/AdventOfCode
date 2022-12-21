#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 15.
#
# Code author: Russell A. Edson
# Date last modified: 21/12/2022

import re

# Read in puzzle input:
with open('day15.txt') as file:
    sensor_readings = [line.strip() for line in file]

# We note the locations of sensors and their closest beacons
# (as measured by the Manhattan distance metric)
def manhattan(pair1, pair2):
    """The Manhattan distance between the two coordinate pairs."""
    return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])
sensors = set()
beacons = set()
sensors_beacons = {}
sensors_dists = {}
#xs = []
#ys = []

for line in sensor_readings:
    coordinates = list(map(int, re.findall(r'[-]*\d+', line)))
    x1, y1, x2, y2 = coordinates
    #xs = xs + [x1, x2]
    #ys = ys + [y1, y2]
    sensors.add((x1, y1))
    beacons.add((x2, y2))
    sensors_beacons[(x1, y1)] = (x2, y2)
    sensors_dists[(x1, y1)] = manhattan((x1, y1), (x2, y2))

#minx = min(xs)
#maxx = max(xs)
#miny = min(ys)
#maxy = max(ys)

# Part 1 has us checking along the line y=2000000 to determine the
# locations where beacons cannot be present (because they would be
# closer to a sensor than any of the other beacons). We can do this
# quickly by mathematically working out the overlap between the line
# at y=2000000 and the radial extent of a given sensor:
#   If the sensor at (x1, y1) has radial extent n and we want to
#   determine the intercept of the bounds of the extent with the line
#   y=c, then:
#     - if c < y1 - n or c > y1 + n, no intersection at all. Else:
#     - if y1 >= c, the line intersects at x = x1 +/- (n + c + - y1),
#     - if y1 <= c, the line intersects at x = x1 +/- (n - c + + y1).
# So we can devise a function that returns the spatial extent in the
# x direction across the line y=2000000 for a given sensor.
# (Note that strictly we should flip the y-coordinates since y
# increases as we go down in the given axes system, but by symmetry
# it doesn't actually matter.)
def xs_along_line(sensor, c):
    """Return the extent for the sensor radius intersected with y=c."""
    x1, y1 = sensor
    n = sensors_dists[tuple(sensor)]

    if c < y1 - n or c > y1 + n:
        return []
    elif y1 >= c:
        return [x1 -(n + c - y1), x1 + (n + c - y1)]
    else:
        return [x1 -(n - c + y1), x1 + (n - c + y1)]

# We can then use this to get the extent for all the sensors,
# (and hence the places where there can be no beacon), making sure
# to account for the overlap and excluding any beacons that are
# already there.
c = 2000000

covered_points = set()
beacon_points = set()
for beacon in beacons:
    if beacon[1] == c:
        beacon_points.add(beacon[0])
        covered_points.add(beacon[0])
for sensor in sensors:
    extent = xs_along_line(sensor, c)
    if len(extent) > 0:
        for point in range(extent[0], extent[1] + 1):
            covered_points.add(point)
print(len(covered_points) - len(beacon_points))

# For Part 2, we are given that the distress beacon has coordinates
# in 0 <= x, y <= 4000000, and we need to determine the only
# position for the beacon and find its tuning frequency:
def tuning_frequency(beacon):
    """Return the tuning frequency for the beacon."""
    return 4000000*beacon[0] + beacon[1]

# In this case, counting each of the points on their own is
# very inefficient. But we can use a heuristic here: we are given
# that there is exactly one location in 0 <= x, y <= 4000000 that
# is not detected by any sensor, so we actually need only consider
# intersections of the circles just beyond the radial extent of
# the sensors. That is, the beacon location will be exactly one
# distance unit away from at least one of the sensors. It is quicker
# to check all of these candidate positions for each sensor.

# We can code a function to get the points just
# beyond the boundary of a sensor:
def just_beyond(sensor):
    """Return all of the points that are just beyond the sensor."""
    x0, y0 = sensor
    radius = sensors_dists[sensor]
    xmin = sensor[0] - radius - 1
    xmax = sensor[0] + radius + 1
    ymin = sensor[1] - radius - 1
    ymax = sensor[1] + radius + 1

    points = set()
    for i in range(0, xmax - x0):
        points.add((xmin + i, y0 - i))
        points.add((x0 + i, ymin + i))
        points.add((xmax - i, y0 + i))
        points.add((x0 - i, ymax - i))
    return points

# And given a point, we want to be able to check whether it is
# in the range of a given sensor:
def in_range_of_sensor(sensor, point):
    """True if point is within the radial extent of sensor."""
    x, y = point
    radius = sensors_dists[sensor]
    xmin = sensor[0] - radius
    xmax = sensor[0] + radius
    ymin = sensor[1] - radius
    ymax = sensor[1] + radius

    if x < xmin or x > xmax:
        return False
    elif y < ymin or y > ymax:
        return False
    else:
        xmin2, xmax2 = xs_along_line(sensor, y)
        return xmin2 <= x and x <= xmax2

def in_range(point):
    """True if point is within the radial extent of at least one sensor."""
    in_range = False
    for sensor in sensors:
        if in_range_of_sensor(sensor, point):
            in_range = True
            break
    return in_range

def outside_range(point):
    """True if point is outside the range of a sensor, and in [0, 4000000]."""
    x, y = point
    valid_x = 0 <= x and x <= 4000000
    valid_y = 0 <= y and y <= 4000000
    return not in_range(point) and valid_x and valid_y

# So now we simply loop over all of the sensors.
for sensor in sensors:
    boundary = just_beyond(sensor)
    filtered = [point for point in boundary if outside_range(point)]
    if len(filtered) > 0:
        # Done: we've found the point.
        point = filtered.pop()
        break

print(point)
print(tuning_frequency(point))
