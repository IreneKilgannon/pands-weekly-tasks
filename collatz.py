# Asks the user to input any positive integer.
# Outputs the following:
    # if number is even, divide by 2.
    # if number is odd, multiply x 3 and add 1.
# Have the program end when value is 1.
# This is called the Collatz Conjecture. 
# Author: Irene Kilgannon

# Modified script to print an error message if the number entered was not a positive integer.

try:
    # Ask the user to input a positive integer. 
    number = int(input("Please enter a positive integer: "))

    # If number a less than or equal to 0 is entered, print an error message. 
    if number <= 0:
        print(f"Error. You entered {number}, which is not a positive integer.")

    else:
        # Generate an empty list called numbers, to which we will append the numbers generated from the for loop.
        numbers = []
        # Append the number to the numbers list.
        numbers.append(number)
        # A for loop to carry out the required calculations.
        for number in numbers:
            # Break out of the loop when the number is equal to 1.
            if number == 1:
                break

            # Check if the number is even.
            elif number % 2 == 0:
                # Divide the number by two if it is even. Append the result to the numbers list.
                # Using floor division as I want the answer as an integer.
                numbers.append(number//2)

            else:
                # For odd numbers append the result of number*3 + 1 to the numbers list.
                numbers.append(number*3 + 1)

        # Iterate through the values in the numbers list.
        for value in numbers:
        # use the end paramater to print the values in numbers list on the same line.
            print(f'{value} ', end = '')

except ValueError:
    print(f'Error. Number must be an integer.')
