# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function that do not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon


# Input
x = float(input("Please enter a positive number: "))

# Need to guess a starting approximation for the square root.

# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$

# The equation for calculating the square root using Newton's equation is 0.5 * (approximation + x/approximation)


def square_root():
    approximation = 0.5 * (x + x/x)
    better_approximation = 0.5 * (approximation + x/approximation)
    while abs(better_approximation - approximation) > 0.0001:
        even_better = 0.5 * (better_approximation + x/better_approximation)
        return even_better

print(f"The square root of {x} is {square_root()}")