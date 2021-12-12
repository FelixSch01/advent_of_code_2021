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
diagnostic_data = []
for line in file.readlines():
    diagnostic_data.append(line.rstrip())


# close file
file.close()

# This function is supposed to calculate the power consumption, which
# is the product of the gamma and epsilon rates. The gamma rate is the
# most common bit in the given data and the epsilon rate is the least
# common bit. The power consumption is returned in base 10.
# This function assumes the length of the data stays constant with the
# length of the first entry over all the lines.
def part_one(data):
    gamma = [None] * len(data[0])
    epsilon = [None] * len(data[0])
    i = 0
    while i < len(data[0]):
        sum_0, sum_1 = 0, 0
        for line in data:
            if line[i] == "0":
                sum_0 += 1
            elif line[i] == "1":
                sum_1 += 1
        if sum_0 > sum_1:
            gamma[i] = "0"
            epsilon[i] = "1"
        elif sum_1 > sum_0:
            gamma[i] = "1"
            epsilon[i] = "0"
        i += 1
    return int("".join(gamma), base=2) * int("".join(epsilon), base=2)

# display the results
print("result for part_one: ", part_one(diagnostic_data))