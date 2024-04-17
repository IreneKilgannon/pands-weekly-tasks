# Pands Weekly Tasks

Author: Irene Kilgannon

Student ID: G00220627

This respository contains the weekly tasks assignments for the Programming and Scripting module for the H. Dip in Science in Data Analytics, Atlantic Technological University.

The aim of programming and scripting module is to teach the basics of python to students who have no prior knowledge of programming.

Eight tasks were assigned and each task was written in python using VScode. Some of the more difficult assignments required additional comments and have an associated Jupyter notebook. These are shown in the table below.


| Week |File.py |Jupyter notebook (if any)|
|-------|--------|-----|
|1 |[helloworld.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/helloworld.py)|     -    |
|2 |[bank.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/bank.py)| -  |
|3 |[accounts.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/accounts.py)| [accounts.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/accounts.ipynb)|
|4 |[collatz.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/collatz.py) |-|
|5 |[weekday.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/weekday.py)|[weekday.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/weekday.ipynb) |
|6|[squareroot.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/squareroot.py)|[squareroot.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/squareroot.ipynb)|
|7| [es.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/es.py)| [es.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/es.py)|
|8|[plottask.py](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/plottask.py)|[plottask.ipynb](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/plottask.ipynb)|


## Prerequisites
***

__Step 1__ Download and install [Anaconda](https://www.anaconda.com/download). Anaconda is a Python distributon and comes with pre-installed packages. 

__Step 2__ Download and install [Visual Studio Code](https://code.visualstudio.com/).

__Step 3__ Each file was written in VScode and pushed to [my GitHub account](https://github.com/IreneKilgannon/pands-weekly-tasks/tree/main) for assessment.

To clone from GitHub enter the following in the command line:

    git clone https://github.com/IreneKilgannon/pands-weekly-tasks.git

To update the repository on your machine, in the command line enter:
    git pull


## Description of each task with references.
***

__Week 1 helloworld.py__

_Task:_ Write a program that prints Hello World!

_Output_

    Hello World!

_References_

1. [Python-print-function](https://www.datacamp.com/tutorial/python-print-function)


__Week 2 bank.py__

_Task:_ Prompt the user to read in two money amounts in cents, sum the amounts and print the answer in euro and cents in the format €0.00.

_Output_

    Enter amount1 (in cent):  65
    Enter amount2 (in cent): 180
    The sum of these is €2.45

_References_

1. Floating Point Arithmetic: Issues and Limitations https://docs.python.org/3/tutorial/floatingpoint.html

2. Floor Division in Python https://www.geeksforgeeks.org/floor-division-in-python/

3. Python Modulo in Practice: How to use the % Operator https://realpython.com/python-modulo-operator/


__Week 3 accounts.py__

_Task:_ Read in a 10 character bank account number and output the account number displaying the last 4 digits showing and the first 6 digits replaced with X's.

_Output_

    Please enter a 10 digit account number: 1234567890
    XXXXXX7890

Extra: Modify the program to deal with an account number of any length.

_Output_

    Please enter an account number: 123456
    XX3456

_References_

1. Python strings https://realpython.com/python-strings/. The sections on string indexing, string slicing and modifying strings were especially useful.

2. Python string concatenation https://www.w3schools.com/python/gloss_python_string_concatenation.asp


__Week 4  collatz.py__

_Task:_ Based on the Collatz Conjecture. Ask the user to input any positive integer and output the following: if number is even, divide by 2, if number is odd, multiply x 3 and add 1. Have the program end when value is 1. 

_Output_

If a positive integer is entered the output is:

    Please enter a positive integer: 16
    16 8 4 2 1

If a negative integer is entered the output is:

    Please enter a positive integer: -16
    Error. You entered -16, which is not a positive integer.

If a floating point number is entered the output is:

    Please enter a positive integer: 9.56
    Error. Number must be an integer.

_References_

1. Youtube video from ScienceWorld, Collatz Conjecture 101 (explanation, examples simulation) https://www.youtube.com/watch?v=6MfifYEA-r0

2. Control Flow, A Whirlwind Tour of Python, Jake VanderPlas, pages 37-41

3. Looping through items in a list https://www.w3schools.com/python/gloss_python_loop_list_items.asp

4. Python end parameter in print() https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

5. Exploring the Collatz Conjecture with Python https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233


__Week 5 weekday.py__

_Task:_ Write a program that outputs whether or not today is a weekday. If it is a weekday output is "Yes, unfortunately today is a weekday". If it is the weekend output is "It is the weekend, yah!"

_Output_

At weekend:

    It is the weekend, yah!

On a weekday:

    Yes, unfortunately today is a weekday.

_References_

1. Datetime - Basic date and time types https://docs.python.org/3/library/datetime.html

2. Python datetime module https://www.geeksforgeeks.org/python-datetime-module/

3. isocalendar() Function of Datetime.date Class in Python https://www.geeksforgeeks.org/isocalendar-function-of-datetime-date-class-in-python/

4. Use Python DateTime to Work with Dates and Times https://realpython.com/python-datetime/

5. Python get Current Date |date.today() and more https://ioflood.com/blog/python-get-current-date/


__Week 6 squareroot.py__

_Task:_ Calculate the square roots using the Newton Method.

_Output_

    Please enter a positive number: 14.5
    The square root of 14.5 is approx. 3.8

If a negative number is entered:

    Please enter a positive number: -9
    Error: The number entered must be a posive number. You entered -9.0.

_References_

1. [Newton-Raphson Method](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html#:~:text=The%20Newton%2DRaphson%20Method%20of,)

2. Explanation of the python square root function from realpython.com https://realpython.com/python-square-root-function/

3. Youtube video: Dubious insights, Worlds Fastest Square Root: Newton's Method https://www.youtube.com/watch?v=FpOEx6zFf1o

4. Square roots via Newton's method https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

5. Learn How to Write Markdown & LaTeX in the Jupyter Notebook https://towardsdatascience.com/write-markdown-latex-in-the-jupyter-notebook-10985edb91fd

6. Python round() function https://www.w3schools.com/python/ref_func_round.asp

7. A much neater, concise method of using Newton's equation to calculate square roots than what I did. Ppython Square Root https://www.kodeclik.com/python-square-root/. Why didn't I think of this?!


__Week 7 es.py__

_Task:_ Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

__Output__

    In the command line:
    PS C:\Users\Irene\Desktop\pands\pands-weekly-tasks> python es.py moby-dick.txt
    115002

Error message for incorrect number of arguments entered in the command line.

    PS C:\Users\Irene\Desktop\pands\pands-weekly-tasks> python es.py moby-dick.jpg moby-dick.txt
    Error: One txt file is required, 2 were entered.

Error message for incorrect file type, file type must be txt.

    PS C:\Users\Irene\Desktop\pands\pands-weekly-tasks> python es.py moby-dick.jpg
    Error: File format must be .txt. File format given was .jpg.

Error message for file not found.
    PS C:\Users\Irene\Desktop\pands\pands-weekly-tasks> python .\es.py moby.txt
    Error: That file was not found.


_References_

1. Link to the moby dick text file. [moby-dick.txt](https://courses.cs.washington.edu/courses/cse390c/22sp/lectures/moby.txt)

2. How to download files with URLs from python https://realpython.com/python-download-file-from-url

3. Python string count() method https://www.w3schools.com/python/ref_string_count.asp

4. Command line arguments https://cs.stanford.edu/people/nick/py/python-command.html#:~:text=The%20command%20line%20is%20a,called%20%22command%20line%20arguments%22

5. Argument parsing in python https://www.datacamp.com/tutorial/argument-parsing-in-python

6. Python - Command Line arguments |sys.argv https://www.youtube.com/watch?v=ZQ9JO0e9468

7. BroCode, Python Read a File https://www.youtube.com/watch?v=LpZmZs2_BC4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=40

8. Python os.path.splitext() method https://www.geeksforgeeks.org/python-os-path-splitext-method/

9. Python try and except https://www.w3schools.com/python/python_try_except.asp 


__Week 8 plottask.py__

_Task:_ Write a program that displays (on the one set of axes):
* a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2
* and a plot of the function h(x) = x^3 in the range of 0 to 10

_Output_

![Plot of Histogram](https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/plottask.png)

_References_

1. How to Plot Normal Distribution over Histogram in Python https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/

2. Python Histogram Plotting: NumPy, Matplotlib, pandas & Seaborn https://realpython.com/python-histograms/

3. Datacamp course, Introduction to Data Visualization with Matplotlib https://app.datacamp.com/learn/courses/introduction-to-data-visualization-with-matplotlib

4. Setting a limit on the x-axis, matplotlib.pyplot.xlim https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html

5. Range() as an argument into plt.hist() function (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

6. List of named colours in matplotlib https://matplotlib.org/stable/gallery/color/named_colors.html



## Get help

If you have any questions or queries you can contact me at g00220627@atu.ie or alternatively submit [an issue](https://github.com/IreneKilgannon/DataAnalytics/issues).
