# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function that does not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon

# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$

# The equation for calculating the square root using Newton's equation is 0.5 * (approximation + a/approximation), where a = number whose square root we need to calculate.

# Ask the user to input a number whose square root we want to calculate.
# Variable is saved as a floating point number.
a = float(input("Please enter a positive number: "))


# Define a square root function.
def sqrt():
    '''This function will calculate approximate square roots using Newton's equation.'''
    # Generate an empty list
    estimates = []

    # The first estimate of the square root
    approximation = a/2

    # Append it to the estimates list
    estimates.append(approximation)

    # A for loop to iterate through the equation.
    for estimate in estimates:
        # Get a new estimate using Newton's equation. x<sub>n</sub> = estimates[-1].
        estimate = 0.5 * (estimates[-1] + a/(estimates[-1]))

        # Append it to the estimates list
        estimates.append(estimate)

        # When the absolute value between the last two items in the list is < 0.00000001, break out of the loop
        if abs(estimates[-2] -estimates[-1]) < 0.00000001:
            break
        
    # The estimate for the square root is the last value in the list.
    return round(estimates[-1], 1)

# Output
# Check that the number entered is a positive number.
if a <= 0:
    # Print error message if number is not positive. 
    print(f'Error: The number entered must be a posive number. You entered {a}.')
else:
    # Print the square root of the number entered.
    print(f"The square root of {a} is approx. {sqrt()}")

# Link to the jupyter notebook: https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/squareroot.ipynb