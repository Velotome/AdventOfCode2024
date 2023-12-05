import re
import math

data = open("input.txt", "r").read().split("\n")
rgb = [12, 13, 14] # number of cube for each color


# get the max number of cube for each color in a game
# format : bag = {'r': 0, 'g': 0, 'b': 0}
def getGameScore(line):
    bag = {'r':0, 'g':0, 'b':0}
    for num, color in re.findall(r'(\d+) (\w)', line):
        bag[color] = max(bag[color], int(num))
    return bag

# Main loop
id = 0
result = 0
for line in data:
    id += 1
    bag = getGameScore(line)

    # if the number of cube for each color is less than the number of cube for each color
    if bag['r'] <= rgb[0] and bag['g'] <= rgb[1] and bag['b'] <= rgb[2]:
        result += id

print(result)