import re

# bug somewhere in the code
# Final value isn't correct, missing some values

data = open("input.txt", "r").read().split("\n")

# Part 1 : Find all symbols
symbols = {}
for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] not in "0123456789.":
            symbols[(x,y)] = []


# Part 2 : Find all numbers in intersectioon with symbols
edge = []
row = 0
for line in data:
    row += 1
    for number in re.finditer(r'\d+', line):
        # compute all the coordinates that are considered "next to" the number
        edge = {(row, c) for r in (row-1, row, row+1) for c in range(number.start()-1, number.end()+1)}
        
        for o in edge & symbols.keys():
            symbols[o].append(int(number.group()))

print(sum(sum(p) for p in symbols.values()))

