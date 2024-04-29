# Write a program that displays a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
# and a plot of the function h(x) = x^3 in the range of 0 to 10
# on the one set of axes
# Save copy of plot on Github
# Author Irene Kilgannon

import numpy as np
import matplotlib.pyplot as plt


# Set a seed, not required as part of task but it will make it easier to track any changes to the program.
np.random.seed(2)

# Inputs into the normal(loc = mean, scale = standard deviation, size = no. of values)
data = np.random.normal(loc = 5, scale = 2, size = 1000)

# Generate a histogram.
plt.hist(data, range = (0, 10), color = 'mediumorchid', edgecolor = 'black')

# Plot the function h(x) = x^3 in the range of 0 to 10

# Generate x points. Endpoint is excluded.
x_points = np.array(range(0, 11))

# Generate the y-points. y = x cubed.
y_points = x_points**3

# Line plot of the function
plt.plot(x_points, y_points, color = 'turquoise', marker = 'o')

# Add title and label x and y axis.
plt.title("Histogram of Normal Distribution and Lineplot of h(x) = x^3")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend(["h(x) = x^3","Normal Distribution"])

# Save the plot as a png file
plt.savefig("plottask.png")

# Display the plot on screen
plt.show()


# Link to the Jupyter notebook for references and additional comments https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/plottask.ipynb
