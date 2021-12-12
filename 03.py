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

# Part two is similar to part one. We want to compute the life support rating
# of our vessel. In order to do that, we have to compute the most common value 
# for each bit of diagnostic data, and only keep the lines with that value
# at that position, then repeat until there is just one number left. This
# number is the oxygen generator rating. There is also a CO2 scrubber rating,
# which is computed the same way, except that only the lines with the least
# common value are kept.
def part_two(data):
    return int(part_two_helper(data, "more"), base=2) * int(part_two_helper(data, "fewer"), base=2)
def part_two_helper(data, bit_criteria):
    if len(data) < 1:
        return
    elif len(data) == 1:
        return data[0]

    all_0, all_1 = [], []
    for line in data:
        if line[0] == "0":
                all_0.append(line[1:])
        elif line[0] == "1":
                all_1.append(line[1:])

    if bit_criteria == "more":
        if len(all_0) > len(all_1):
            return "0" + part_two_helper(all_0, bit_criteria)
        elif len(all_0) == len(all_1):
            return "1" + part_two_helper(all_1, bit_criteria)
        elif len(all_1) > len(all_0):
            return "1" + part_two_helper(all_1, bit_criteria)

    if bit_criteria == "fewer":
        if len(all_0) > len(all_1):
            return "1" + part_two_helper(all_1, bit_criteria)
        elif len(all_0) == len(all_1):
            return "0" + part_two_helper(all_0, bit_criteria)
        elif len(all_1) > len(all_0):
            return "0" + part_two_helper(all_0, bit_criteria)
        
# display the results
print("result for part one: ", part_one(diagnostic_data))
print("result for part two: ", part_two(diagnostic_data))