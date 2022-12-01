#!/usr/bin/python3

# Python code for the Advent of Code 2015, Day 2.
#
# Code author: Russell A. Edson
# Date last modified: 01/12/2022

# Read in puzzle input
with open('day02.txt') as file:
    dimensions = [list(map(int, line.strip().split('x'))) for line in file]

# Presents have dimensions listed in [length, width, height], and
# the face areas are length*width, width*height, height*length.
face_areas = [[l*w, w*h, h*l] for [l, w, h] in dimensions]

# Each face appears twice, and the smallest area face is added
# for extra slack
smallest_faces = list(map(min, face_areas))
surface_areas = [2*(a + b + c) for a, b, c in face_areas]
wrap = [slack + area for slack, area in zip(smallest_faces, surface_areas)]

# Part 1 simply asks for the total number of square feet of wrapping
# paper needed.
print(sum(wrap))

# Part 2 requires the perimeters of the faces and the cubic volume of
# the presents:
face_perimeters = [[2*(l+w), 2*(w+h), 2*(h+l)] for [l, w, h] in dimensions]
smallest_perimeters = list(map(min, face_perimeters))
volumes = [l*w*h for [l, w, h] in dimensions]

ribbon = [side + bow for side, bow in zip(smallest_perimeters, volumes)]
print(sum(ribbon))
