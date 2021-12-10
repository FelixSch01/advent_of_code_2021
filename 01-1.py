#!/bin/python3
 
# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

# imports
import sys as s

# handle arguments
if len(s.argv[1:]) == 1:
    file = s.argv[1]
else:
    print('usage: 01-1.py <input file>')

# read input file
depth_measurements = file.readlines()

# loop over numbers
i, result = 0
while(i < len(depth_measurements)):
    if i == 0:
        continue
    if depth_measurements[i] > depth_measurements[i - 1]:
        result += 1
    