# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function that do not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon



# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$
# Need to guess an answer for the square root e.g. if trying to calculate the square root of 2, we could guess that the answer might be 1.


# Back to the drawing board. 

x = float(input("Please enter a positive number: "))
guess = x/2
estimate = 

def square_root(number):

square_root = estimate

print(f"The square root of {x} is approx {square_root}")

