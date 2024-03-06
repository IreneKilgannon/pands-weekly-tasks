# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function that do not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon


# Input
144


# Need to guess a starting approximation for the square root.

# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$

# The equation for calculating the square root using Newton's equation is 0.5 * (approximation + x/approximation)


x = float(input("Please enter a positive number: "))

def square_root():
    estimates = []
    approximation = x/2
    estimates.append(approximation)
    for estimate in estimates:
        estimate = 0.5 * (estimates[-1] + x/(estimates[-1]))
        estimates.append(estimate)
        if abs(estimates[-2] -estimates[-1]) < 0.0000001:
            break
    return estimates

print(square_root())
