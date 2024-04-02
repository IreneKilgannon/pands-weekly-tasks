# Pands Weekly Tasks

Author: Irene Kilgannon

This respository contains the weekly tasks assignments for the module, Programming and Scripting for the H. Dip in Science in Data Analytics, Atlantic Technological University.

The overall aim of programming and scripting module is to teach the basics of Python programming.

Eight tasks were assigned and each task was written in python using VScode. Some of the trickier assignments, that required additional comments have an associated Jupyter notebook ,as shown in the table below.


| Week |File.py |Jupyter notebook (if any)|
|-------|--------|-----|
|1 |[helloworld.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/helloworld.py)|         |
|2 |[bank.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/bank.py)|   |
|3 |[accounts.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/accounts.py)| [accounts.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/accounts.ipynb)|
|4 |[collatz.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/collatz.py) |
|5 |[weekday.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/weekday.py)|[weekday.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/weekday.ipynb) |
|6|[squareroot.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/squareroot.py)|[squareroot.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/squareroot.ipynb)|
|7| [es.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/es.py)| [es.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/es.py)|
|8|[plottask.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/plottask.py)|[plottask.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/plottask.ipynb)|


## Prerequisites

Download and install [Anaconda](https://www.anaconda.com/download).

Download and install [Visual Studio Code](https://code.visualstudio.com/).


## Description of each task and references.


__Week 1 helloworld.py__

Write a program that prints Hello World!

[Python-print-function](https://www.datacamp.com/tutorial/python-print-function)


__Week 2 bank.py__

Prompt the user and read in two money amounts in cents, sum the amounts and print the answer in euro and cents €0.00.

[Floating point errors](https://docs.python.org/3/tutorial/floatingpoint.html)

[Floor division](https://www.geeksforgeeks.org/floor-division-in-python/)

[Modulo](https://realpython.com/python-modulo-operator/#modulo-operator-with-float)


__Week 3 accounts.py__

Read in a 10 character bank account number and outputs the account number displaying the last 4 digits showing and the first 6 digits replaced with X's.

Extra: Modify the program to deal with an account number of any length.

[Python strings](https://realpython.com/python-strings/) The sections on string indexing, string slicing and modifying strings were particularily useful.

[Python string concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp)


__Week 4  collatz.py__

Based on the Collatz Conjecture. Asks the user to input any positive integer and outputs the following: if number is even, divide by 2, if number is odd, multiply x 3 and add 1. Have the program end when value is 1.

Short video about the [Collatz conjecture](https://www.youtube.com/watch?v=6MfifYEA-r0)

Control Flow, A Whirlwind Tour of Python, Jake VanderPlas, pages 37-41

[Looping through items in a list](https://www.w3schools.com/python/gloss_python_loop_list_items.asp)

[Python end parameter in print()](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/)

[Collatz from defining a function and using a while loop](https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233)


__Week 5 weekday.py__

Write a program that outputs whether or not today is a weekday. If it is a weekday output is "Yes, unfortunately today is a weekday". If it is the weekend output is "It is the weekend, yah!"

[datetime module](https://docs.python.org/3/library/datetime.html)

https://www.geeksforgeeks.org/python-datetime-module/

[isocalendar](https://www.geeksforgeeks.org/isocalendar-function-of-datetime-date-class-in-python/)

[Python DateTime](https://realpython.com/python-datetime/)

[DateTime Variables in Python and Pandas](https://www.analyticsvidhya.com/blog/2020/05/datetime-variables-python-pandas/)

[date.today()](https://ioflood.com/blog/python-get-current-date/)

[Python DateTime: A simple guide with 39 Code Examples](https://www.dataquest.io/blog/python-datetime/)


__Week 6 squareroot.py__

Calculate the square roots using the Newton Method.

[Newton-Raphson Method](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html#:~:text=The%20Newton%2DRaphson%20Method%20of,)

Explanation of the python square root function from [realpython.com](https://realpython.com/python-square-root-function/)

Youtube video: [Dubious insights, Worlds Fastest Square Root: Newton's Method](https://www.youtube.com/watch?v=FpOEx6zFf1o)

[Square roots via Newton's method](https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf)

[Writing mathematical formulae in markdown](https://towardsdatascience.com/write-markdown-latex-in-the-jupyter-notebook-10985edb91fd)

A much neater, concise method of using Newton's equation to calculate square roots than what I did. [python square root](https://www.kodeclik.com/python-square-root/). Why didn't I think of this?!


__Week 7 es.py__

Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

Link to the moby dick text file. [moby-dick.txt](https://courses.cs.washington.edu/courses/cse390c/22sp/lectures/moby.txt)

How to [download files with URLs from python](https://realpython.com/python-download-file-from-url)

[Python string count() method](https://www.w3schools.com/python/ref_string_count.asp)

[Command line arguments](https://cs.stanford.edu/people/nick/py/python-command.html#:~:text=The%20command%20line%20is%20a,called%20%22command%20line%20arguments%22)

[Argument parsing in python](https://www.datacamp.com/tutorial/argument-parsing-in-python)

YouTube video on [Sys.argv](https://www.youtube.com/watch?v=ZQ9JO0e9468)

YouTube video on [Try and Except](https://www.youtube.com/watch?v=LpZmZs2_BC4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=40)

[os.path.splitext() method](https://www.geeksforgeeks.org/python-os-path-splitext-method/)

[Python read a file](https://www.youtube.com/watch?v=LpZmZs2_BC4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=39)

[Python try and except](https://www.w3schools.com/python/python_try_except.asp)


__Week 8 plottask.py__

Write a program that displays (on the one set of axes):
* a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
* and a plot of the function h(x) = x^3 in the range of 0 to 10

[Normal Distribution](https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/)

[Python Histograms](https://realpython.com/python-histograms/)

Datacamp course [Introduction to Data Visualization with Matplotlib](https://app.datacamp.com/learn/courses/introduction-to-data-visualization-with-matplotlib)

[Setting a limit on the x-axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html)

[Colours in matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html)


## Get help

If you have any questions or queries contact me at g00220627@atu.ie or alternatively submit [an issue](https://github.com/IreneKilgannon/DataAnalytics/issues).
