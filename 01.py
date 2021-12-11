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

# read input file and convert to int array
depth_measurements = []
for line in file.readlines():
    depth_measurements.append(int(line.rstrip()))

# close file
file.close()

# Loop over numbers to calculate the amount of times a number is bigger
# compared to the previous number. The first number is not counted, since
# there is no preceding number.
def part_one(numbers):
    i = 0
    result = 0
    while(i < len(numbers)):
        if i == 0:
            i += 1
            continue
        if numbers[i] > numbers[i - 1]:
            result += 1
        i += 1
    return result

# the same as part one, except this time, the sum of the first number and
# the following two is compared to the sum of the next number and the 
# following two. The first sum is not counted, since there is no previous
# sum. the last sum are the three numbers at the end of the list.
def part_two(numbers):
    i = 0
    sums = []
    while(i < len(numbers) - 2):
        sums.append(numbers[i] + numbers[i + 1] + numbers[i + 2])
        i += 1
    return part_one(sums)

# display the results
print("result for part one:    " + str(part_one(depth_measurements)))
print("result for part two:    " + str(part_two(depth_measurements)))

# exit the program
sys.exit(0)