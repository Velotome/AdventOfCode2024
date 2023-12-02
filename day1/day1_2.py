data = open("input.txt", "r").read().split("\n")

numbers = ["1","2","3","4","5","6","7","8","9"]
written_numbers = ["one","two","three","four","five","six","seven","eight","nine"]

result = 0

# main loop
for line in data:
    line_temp = line
    
    # Deals with written numbers

    for i in range(len(written_numbers)):
        # replace the written number with the first letter of the number the digit + last letter of the number
        line = line.replace(written_numbers[i], written_numbers[i][0] + numbers[i] + written_numbers[i][-1])


    # Compute result

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