#!/usr/bin/python3

# Python code for the Advent of Code 2019, Day 6.
#
# Code author: Russell A. Edson
# Date last modified: 10/12/2022

# Read in puzzle input
with open('day06.txt') as file:
    orbits = [line.strip().split(')') for line in file]

# For Part 1, we want to find the direct and indirect orbits for
# the system. We can represent this with a tree data structure:
class Tree:
    """A tree data structure, with a parent node and child nodes."""
    def __init__(self, label):
        self.label = label
        self.parent = None
        self.children = []

    def __str__(self):
        parent_label = self.parent.label if self.parent is not None else ''
        children_label = list(map(lambda node: node.label, self.children))
        return ' -> '.join([parent_label, self.label, str(children_label)])

nodes = {}

for orbit in orbits:
    body, satellite = orbit
    body_ptr = nodes.get(body, None)
    if body_ptr is None:
        nodes[body] = Tree(body)
        body_ptr = nodes[body]
    satellite_ptr = nodes.get(satellite, None)
    if satellite_ptr is None:
        nodes[satellite] = Tree(satellite)
        satellite_ptr = nodes[satellite]
    body_ptr.children.append(satellite_ptr)
    satellite_ptr.parent = body_ptr

# Then to find the number of direct and indirect orbits for a given
# node, we simply iterate back through parents until we reach the
# base node.
def orbits_count(node):
    """Return the total number of direct and indirect orbits for node."""
    count = 0
    node_ptr = nodes.get(node, None)
    if node_ptr is not None:
        node_ptr = node_ptr.parent
        while node_ptr is not None:
            count = count + 1
            node_ptr = node_ptr.parent
    return count

# The total orbits for all nodes is:
print(sum(map(orbits_count, nodes.keys())))

# For Part 2, we want to determine the minimum number of orbital
# transfers between YOU and SAN. We can do this by iterating traversals
# back to the root node from YOU and SAN simultaneously: the branch point
# will be the first node in common between both of the traversal paths.
path_YOU = ['YOU']
ptr_YOU = nodes.get('YOU', None)
path_SAN = ['SAN']
ptr_SAN = nodes.get('SAN', None)

branch_point_found = False
while branch_point_found == False:
    if ptr_YOU is not None:
        ptr_YOU = ptr_YOU.parent
    if ptr_YOU is not None:
        path_YOU.append(ptr_YOU.label)
        if ptr_YOU.label in path_SAN:
            branch_point_found = True
            path_SAN = path_SAN[:(path_SAN.index(ptr_YOU.label) + 1)]
            break
    if ptr_SAN is not None:
        ptr_SAN = ptr_SAN.parent
    if ptr_SAN is not None:
        path_SAN.append(ptr_SAN.label)
        if ptr_SAN.label in path_YOU:
            branch_point_found = True
            path_YOU = path_YOU[:(path_YOU.index(ptr_SAN.label) + 1)]
            break

# Then the minimum number of orbital jumps required is simply the
# length of these two paths added (subtracting the starting nodes,
# since we don't count YOU and SAN themselves, and subtracting 1 since
# we are counting the jumps, not the nodes).
print(len(path_YOU[1:]) - 1 + len(path_SAN[1:]) - 1)
