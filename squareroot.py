# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function that do not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon



# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$

# The equation for calculating the square root using Newton's equation is 0.5 * (approximation + x/approximation).

# Input
x = float(input("Please enter a positive number: "))


# Define a square root function
def square_root():
    # Generate an empty list
    estimates = []

    # The first estimate of the square root
    approximation = x/2

    # Append it to the list
    estimates.append(approximation)
    for estimate in estimates:

        # Get a new estimate using the last value in the estimates list.
        estimate = 0.5 * (estimates[-1] + x/(estimates[-1]))

        # Append it to the list
        estimates.append(estimate)

        # When the absolute value between the last two items in the list is < 0.0000001, break out of the loop
        if abs(estimates[-2] -estimates[-1]) < 0.0000001:
            break
        
    # The estimate for the square root is the last value in the list
    return estimates[-1]

# Output
print(f"The square root of {x} is {square_root()}")

