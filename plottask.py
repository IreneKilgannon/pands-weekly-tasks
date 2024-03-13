# Write a program that displays a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
# and a plot of the function h(x) = x^3 in the range of 0 to 10
# on the one set of axe
# Author Irene Kilgannon

import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(5, 2, 1000)

plt.hist(data)
plt.show()

x_points = np.array(range(0, 10))
y_points = x_points*x_points*x_points

plt.plot(x_points, y_points)
plt.show()