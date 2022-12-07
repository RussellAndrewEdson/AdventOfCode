#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 7.
#
# Code author: Russell A. Edson
# Date last modified: 07/12/2022

import re

# Read in puzzle input
with open('day07.txt') as file:
    output = iter([line.strip() for line in file])

# The output consists of commands (moving directories and
# directory listings), together with their output. We keep
# track of the current directory and build up the directory
# structure piece-by-piece.
current_directory = ['/']
structure = {'/': {}}

def mkdir(dir):
    """Make a new directory 'dir' in the current directory."""
    dir_pointer = structure[current_directory[0]]
    for directory in current_directory[1:]:
        dir_pointer = dir_pointer[directory]
    dir_pointer[dir] = {}

def touch(file, size):
    """Make a new file 'file' with size 'size' in the current directory."""
    dir_pointer = structure[current_directory[0]]
    for directory in current_directory[1:]:
        dir_pointer = dir_pointer[directory]
    dir_pointer[file] = size

command = next(output)
while command != None:
    read_command = False
    command = re.split(r'\s+', re.sub(r'\$\s+', '', command))
    if command[0] == 'cd':
        if command[1] == '/':
            current_directory = ['/']
        elif command[1] == '..':
            current_directory.pop()
        else:
            current_directory.append(command[1])
    elif command[0] == 'ls':
        ls_output = []
        ls_line = next(output, None)
        while ls_line != None and read_command == False:
            if ls_line.startswith('$'):
                read_command = True
                command = ls_line
            else:
                ls_output.append(ls_line)
                ls_line = next(output, None)
        for line in ls_output:
            line = re.split(r'\s+', line)
            if line[0] == 'dir':
                mkdir(line[1])
            else:
                touch(line[1], line[0])
    if read_command == False:
        command = next(output, None)

# With the structure read in, we can traverse it to get the
# sizes of each directory in turn.
def total_size(node):
    """Return the total size of the given node (directory/file)."""
    listing = list(node.values())
    size = 0
    for item in listing:
        if isinstance(item, dict):
            size = size + total_size(item)
        else:
            size = size + int(item)
    return size

directories_to_check = [['/']]
directory_sizes = {}
while len(directories_to_check) > 0:
    next_directory = directories_to_check.pop()
    dir_name = ''.join(list('/'.join(next_directory))[1:])
    if dir_name == '':
        dir_name = '/'

    dir_pointer = structure[next_directory[0]]
    for directory in next_directory[1:]:
        dir_pointer = dir_pointer[directory]
    directory_sizes[dir_name] = total_size(dir_pointer)

    # Determine subdirectories
    for item in list(dir_pointer.keys()):
        if isinstance(dir_pointer[item], dict):
            directories_to_check.append(next_directory + [item])

# Finally, Part 1 asks us to find the directories with a total size of
# at most 100,000, and sum those up.
print(sum(filter(lambda size: size < 100000, directory_sizes.values())))

# For Part 2, we need to free up at least 30,000,000 bytes given
# a total disk space size of 70,000,000, by deleting the smallest
# directory that gives us enough space. Now that we have the directory
# sizes, we simply loop through to find the smallest one.
free_space = 70000000 - total_size(structure)
space_deficit = 30000000 - free_space

smallest_dir = '/'
smallest_dir_size = directory_sizes[smallest_dir]
for directory in directory_sizes:
    directory_size = directory_sizes[directory]
    if directory_size >= space_deficit:
        if directory_size <= smallest_dir_size:
            smallest_dir = directory
            smallest_dir_size = directory_size

print(smallest_dir + ': ' + str(smallest_dir_size))
