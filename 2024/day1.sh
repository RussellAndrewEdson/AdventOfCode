#!/bin/bash

# Shell script for Day 1 of the 2024 Advent of Code puzzle.
# (Assume the input file is called 'day1.txt'.)

# Reading in the data
DAY_1_INPUT=$(cat day1.txt | tr -s ' ')
LEFT=$(cut -d' ' -f 1 <<<$DAY_1_INPUT)
RIGHT=$(cut -d' ' -f 2 <<<$DAY_1_INPUT)

# Part 1
LEFT_SORTED=($(sort --numeric-sort <<<$LEFT))
RIGHT_SORTED=($(sort --numeric-sort <<<$RIGHT))

TOTAL_DIST=0
for i in $(seq 0 $((${#LEFT_SORTED[@]} - 1)))
do
  DIST=$((${LEFT_SORTED[i]} - ${RIGHT_SORTED[i]}))
  TOTAL_DIST=$((TOTAL_DIST + ${DIST#-}))
done
echo $TOTAL_DIST

# Part 2
SIMILARITY_SCORE=0
for i in $LEFT
do
  for j in $RIGHT
  do
    [ $j -eq $i ] && SIMILARITY_SCORE=$((SIMILARITY_SCORE + i))
  done
done
echo $SIMILARITY_SCORE
