# Asks the user to input any positive integer
# OUtputs the following:
    # if even, divide by 2
    # if odd, multiply x 3 and add 1
# Have the program end when value is 1

numbers = []

number = int(input("Please enter a positive integer: "))

numbers.append(number)

for number in numbers:
    if number > 1 and number % 2 == 0:
        numbers.append(number//2)
    elif number > 1 and number % 2 == 1:
        numbers.append(number*3 + 1)
    else:
        numbers.append(number)
        break
print(numbers)


# Need to not have a list format
# only one 1 at the end