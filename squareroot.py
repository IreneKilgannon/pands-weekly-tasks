# Write a program that takes a positive floating-point number as input.
# Outputs an approximation of its square root.
# Create own square root function and do not use built in functions. 
# Suggested to look at the newton method of estimating square roots.
# Author: Irene Kilgannon



x = float(input("Please enter a positive number: "))

# $$x_{n+1} = \frac{1}{2}(x_{n}+ \frac{a}{x_{n}})$$
# Need to guess an answer for the square root e.g. if trying to calculate the square root of 2, we could guess that the answer might be 1.

first_guess = x/2
square_roots = []

newton_first_iteration = 0.5 * (first_guess + x/first_guess)
square_roots.append(newton_first_iteration)
print(square_roots)

subsequent_iterations = 0.5 * (square_roots[-1] + x/square_roots[-1])
square_roots.append(subsequent_iterations)
print(square_roots)

subsequent_iterations = 0.5 * (square_roots[-1] + x/square_roots[-1])
square_roots.append(subsequent_iterations)
print(square_roots)

subsequent_iterations = 0.5 * (square_roots[-1] + x/square_roots[-1])
square_roots.append(subsequent_iterations)
print(square_roots)

#newton_first_iteration = subsequent_iterations

#difference = newton_first_iteration - subsequent_iterations
#print(difference)

#while difference <= 0.001:
 #   subsequent_iterations = 0.5 * (newton_first_iteration + x/newton_first_iteration)
 #   subsequent_iterations = newton_first_iteration
  #  subsequent_iterations = 0.5 * (newton_first_iteration + x/newton_first_iteration)
  #  subsequent_iterations = newton_first_iteration
    #subsequent_iterations = 0.5 * (newton_first_iteration + x/newton_first_iteration)

#print(subsequent_iterations)
#Subsequent_iterations1 = 0.5 * (Subsequent_iterations + x/Subsequent_iterations)
#print(Subsequent_iterations1)



#print(first_guess)
#while 
#iteration_plus = (0.5 * (first_guess + x/first_guess))
#print(iteration_plus)





#print(f"The square root of {square_root} is approx {}")

