data = open("input.txt", "r").read().split("\n")

numbers = ["1","2","3","4","5","6","7","8","9"]
written_numbers = ["one","two","three","four","five","six","seven","eight","nine"]

result = 0

for line in data:
    line_numbers = {}
    line_temp = line
    
    # Deals with written numbers
    for i in range(len(written_numbers)):
        while line.find(written_numbers[i]) != -1:
            index = line.find(written_numbers[i])
            line_numbers[index] = int(numbers[i])
            line = line[:index] + " " + line[index + 1:]

    # Deals with digits
    for i in range(len(numbers)):
        while line.find(numbers[i]) != -1:
            index = line.find(numbers[i])
            line_numbers[index] = int(numbers[i])
            line = line[:index] + " " + line[index + 1:]

    # Sorts the dictionary by key
    line_numbers_sorted = dict(sorted(line_numbers.items()))
    line_numbers_list = list(line_numbers_sorted.values())

    result += line_numbers_list[0] * 10 + line_numbers_list[-1]

print(result)