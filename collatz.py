# Asks the user to input any positive integer.
# Outputs the following:
    # if number is even, divide by 2.
    # if number is odd, multiply x 3 and add 1.
# Have the program end when value is 1.
# This is called the Collatz Conjecture. 
# Author: Irene Kilgannon


# Generate an empty list called numbers, to which we will append the numbers generated from the for loop.
numbers = []

# Ask the user to input a positive integer. 
number = int(input("Please enter a positive integer: "))

# If number a negative number is entered, print an error message. 
if number < 0:
    print('The number must be a positive integer. You entered a negative integer.')
    number = int(input("Please enter a positive integer: "))

# Append the number to the numbers list.
numbers.append(number)

# A for loop to carry out the required calculations.
for number in numbers:
    # Break out of the loop when the number is 1.
    if number == 1:
        break

    # Divide the number by two if it is greater that 1 and even. Append the result to the numbers list.
    elif number % 2 == 0:
        numbers.append(number//2)

    # For odd numbers append the result of number*3 + 1 to the list.
    else:
        numbers.append(number*3 + 1)

# use a for loop to get the values in numbers list.
for value in numbers:
    # use the end paramater to print the values in numbers list on the same line.
    print(f'{value} ', end = '')


'''
References

Short video on the Collatz conjecture: https://www.youtube.com/watch?v=6MfifYEA-r0

Control Flow, A Whirlwind Tour of Python, Jake VanderPlas, pages 37-41  or https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/07-Control-Flow-Statements.ipynb

Looping through items in a list: https://www.w3schools.com/python/gloss_python_loop_list_items.asp

Python end parameter in print(): https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

Collatz from defining a function and using a while loop: https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233
'''