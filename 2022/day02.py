#!/usr/bin/python3

# Python code for the Advent of Code 2022, Day 2.
#
# Code author: Russell A. Edson
# Date last modified: 02/12/2022

# Read in puzzle input
with open('day02.txt') as file:
    instructions = [line.strip().split(' ') for line in file]

# The input represents Rock, Paper, Scissors rounds, with
#   'A', 'X' = Rock
#   'B', 'Y' = Paper
#   'C', 'Z' = Scissors.
# We can code a function to determine the score for a given
# hand shape (1 for Rock, 2 for Paper, 3 for Scissors):
def shape_score(hand):
    """Return the score for the given hand shape."""
    score = None
    if hand == 'A' or hand == 'X':
        score = 1
    elif hand == 'B' or hand == 'Y':
        score = 2
    elif hand == 'C' or hand == 'Z':
        score = 3
    return score

# Similarly, a function to return the outcome of a round:
def outcome_score(opponent_hand, your_hand):
    """Return the score for the outcome of the round."""
    score = None
    if your_hand == 'X':
        if opponent_hand == 'A':
            score = 3
        elif opponent_hand == 'B':
            score = 0
        elif opponent_hand == 'C':
            score = 6
    elif your_hand == 'Y':
        if opponent_hand == 'A':
            score = 6
        elif opponent_hand == 'B':
            score = 3
        elif opponent_hand == 'C':
            score = 0
    elif your_hand == 'Z':
        if opponent_hand == 'A':
            score = 0
        elif opponent_hand == 'B':
            score = 6
        elif opponent_hand == 'C':
            score = 3
    return score

# Part 1 asks for the total scores for the instructions.
def score(hands):
    """Return the score for the hands."""
    opponents_hand, your_hand = hands
    return shape_score(your_hand) + outcome_score(opponents_hand, your_hand)

print(sum(map(score, instructions)))

# For Part 2, now 'X' means a loss, 'Y' means a draw, and 'Z' means
# a win, and so the hand has to be determined. We can use the functions
# already coded if we code a rule to turn the second column into the
# value of the hand necessary.
def convert_for_part_2(hands):
    """Return [opponents, yours] as expected by the prior functions."""
    opponents_hand, outcome = hands
    your_hand = None
    if outcome == 'X':
        if opponents_hand == 'A':
            your_hand = 'Z'
        elif opponents_hand == 'B':
            your_hand = 'X'
        elif opponents_hand == 'C':
            your_hand = 'Y'
    elif outcome == 'Y':
        if opponents_hand == 'A':
            your_hand = 'X'
        elif opponents_hand == 'B':
            your_hand = 'Y'
        elif opponents_hand == 'C':
            your_hand = 'Z'
    elif outcome == 'Z':
        if opponents_hand == 'A':
            your_hand = 'Y'
        elif opponents_hand == 'B':
            your_hand = 'Z'
        elif opponents_hand == 'C':
            your_hand = 'X'

    return [opponents_hand, your_hand]

print(sum(map(score, map(convert_for_part_2, instructions))))
