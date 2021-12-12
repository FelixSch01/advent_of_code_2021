#!/bin/python3
 
# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3

# imports
import sys

# handle arguments
if len(sys.argv) == 2:
    file = open(sys.argv[1])
else:
    print('usage: 03.py <input file>')
    sys.exit(-1)

# read input file
diagnostic_data = file.readlines()

# close file
file.close()
