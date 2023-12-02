data = open("input.txt", "r").read().split("\n")

numbers = ["1","2","3","4","5","6","7","8","9","0"]
written_numbers = ["one","two","three","four","five","six","seven","eight","nine","zero"]

result = 0

for line in data:

    # add the first number x 10 starting from the left of the line
    for char in line:
        if char in numbers:
            digit = int(char)
            result += digit * 10
            break

    # add the first number starting from the right of the line
    for char in line[::-1]:
        if char in numbers:
            digit = int(char)
            result += digit
            break

print(result)