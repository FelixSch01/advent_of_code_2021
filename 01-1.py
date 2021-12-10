#!/bin/python3
 
# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

# imports
import sys

# handle arguments
if len(sys.argv) == 2:
    file = open(sys.argv[1])
else:
    print('usage: 01-1.py <input file>')
    sys.exit(-1)
# read input file
depth_measurements = file.readlines()

# Loop over numbers to calculate the amount of times a number is bigger
# compared to the previous number. The first number is excluded.
i = 0
result = 0
while(i < len(depth_measurements)):
    if i == 0:
        i += 1
        continue
    if depth_measurements[i] > depth_measurements[i - 1]:
        result += 1
    i += 1

# display the result
print(result)