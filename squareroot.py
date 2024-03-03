# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function and do not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon



# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$
# Need to guess an answer for the square root e.g. if trying to calculate the square root of 2, we could guess that the answer might be 1.


# Back to the drawing board. 

x = float(input("Please enter a positive number: "))
guess = x/2


def square_root(number):
    estimate = []
    estimate.append(guess)
    improved_estimate = 0.5 * (estimate + x/estimate)
    estimate.append(improved_estimate)
    if abs(estimate[-2]) >= abs(estimate[-1]):
        even_better_estimate = 0.5 * (estimate[-1] + x/estimate[-1])
        estimate.append(even_better_estimate)
        print[estimate]
        return estimate

print(f"The square root of {x} is approx {estimate[-1]}")

