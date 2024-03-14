# Write a program that displays a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
# and a plot of the function h(x) = x^3 in the range of 0 to 10
# on the one set of axe
# truncate at 10 (if needed)
# Save copy of plot on Github
# Author Irene Kilgannon

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123355)
data = np.random.normal(5, 2, 1000)  # inputs into the normal(mean, standard deviation, values)

# Truncate the x-axis at 10  
plt.xlim([0, 10])
#axes.set_ylim([ymin,ymax])

plt.hist(data)

# Plot the function h(x) = x^3 in the range of 0 to 10

# Generate x points
x_points = np.array(range(0, 10))

# Generate the y-points. y = x cubed.
y_points = x_points**3

# Line plot of the function
plt.plot(x_points, y_points, marker = 'v')

# Add title and label x and y axis.

plt.title("Plot of normal distribution and h(x) = x**3")
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.legend(x_points)

# Save the plot as a png file
plt.savefig("plottask.png")

# Display the plot on screen
plt.show()

