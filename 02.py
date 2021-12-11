#!/bin/python3
 
# --- Day 2: Dive! ---
# https://adventofcode.com/2021/day/2

# imports
import sys

# handle arguments
if len(sys.argv) == 2:
    file = open(sys.argv[1])
else:
    print('usage: 02.py <input file>')
    sys.exit(-1)

# read input file and convert to int array
commands = []
for line in file.readlines():
    temp = [line.split(" ")]
    temp[1] = int(temp[1].rstrip())
    commands.append(temp)

# close file
file.close()
