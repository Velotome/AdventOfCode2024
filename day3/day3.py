import re

data = open("input.txt", "r").read().split("\n")

nonSymbols = "0123456789."

# Part 1 : Find all symbols
symbols = {}
for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] not in nonSymbols:
            symbols[(x,y)] = data[y][x]

# Part 2 : Find all numbers
numbers = {}
line_number = 0
for line in data:
    line_number += 1
    for number in re.finditer(r'\d+', line):
        # Store the number in a dict with key as (start_of_number-1, end_of_number+1, line_number)
        numbers[(number.start()-1, number.end()+1, line_number)] = int(str(number.group(0)))
