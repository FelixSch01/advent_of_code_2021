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
steering = []
for line in file.readlines():
    temp = line.split(" ")
    temp[1] = int(temp[1].rstrip())
    steering.append(temp)

# close file
file.close()

# Loop over commands and compute final horizontal position and depth.
# Horizontal position and depth each start at 0, the command 'forward'
# increases the horizontal position by its value, the command 'down'
# increases and the command 'up' decreases depth by its value.
# The final positions get multiplied to compute the desired value.
def part_one(commands):
    horizontal_pos = 0
    depth = 0
    for command in commands:
        if command[0] == "forward":
            horizontal_pos += command[1]
        elif command[0] == "down":
            depth += command[1]
        elif command[0] == "up":
            depth -= command[1]
    return horizontal_pos * depth

# Like part one, but one more variable, aim, comes into play. aim 
# increases by the amount of the 'down' and decreases by the amount of 
# the 'up' command. The 'down' and 'up' commands don't directly influence
# the depth anymore, instead the 'forward' command now increases the depth 
# by its value multiplied with the aim, in addition to its previous function.
def part_two(commands):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for command in commands:
        if command[0] == "forward":
            horizontal_pos += command[1]
            depth += command[1] * aim
        elif command[0] == "down":
            aim += command[1]
        elif command[0] == "up":
            aim -= command[1]
    return horizontal_pos * depth

# display the results
print("result for part one: ", part_one(steering))
print("result for part two: ", part_two(steering))
# exit the program
sys.exit(0)