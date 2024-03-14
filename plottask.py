# Write a program that displays a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
# and a plot of the function h(x) = x^3 in the range of 0 to 10
# on the one set of axe
# truncate at 10 (if needed)
# Save copy of plot on Github
# Author Irene Kilgannon

import numpy as np
import matplotlib.pyplot as plt


# Set a seed, not required as part of task but it will make it easier to see any changes made to the program. Remove before submitting.
np.random.seed(123355)


data = np.random.normal(5, 2, 1000)  # inputs into the normal(mean, standard deviation, values)

# Truncate the x-axis at 10  
plt.xlim(0, 10)

# Generate a histogram.
plt.hist(data, bins = 15, color = 'mediumorchid', edgecolor = 'black')

# Plot the function h(x) = x^3 in the range of 0 to 10

# Generate x points
x_points = np.array(range(0, 10))

# Generate the y-points. y = x cubed.
y_points = x_points**3

# Line plot of the function
plt.plot(x_points, y_points, color = 'turquoise', marker = 'o')

# Add title and label x and y axis.

plt.title("Plot of normal distribution and h(x) = x**3")
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.legend(["function","normal distribution"])

# Save the plot as a png file
plt.savefig("plottask.png")

# Display the plot on screen
plt.show()


# References

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html