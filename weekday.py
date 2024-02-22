# Write a program that outputs whether or not today is a weekday
# If it is a weekday output is "Yes, unfortunately today is a weekday".
# If weekend output "It is the weekend, yah!"
# Author: Irene Kilgannon


# The datetime module is used for handling dates and times in Python.
# As we don't need time for this program, only the date class will be imported.

from datetime import date

# To find today's date, use the built in today() method.
# Use weekday() of class date in the datetime module to extract the day of the week. 

today = date.today().weekday()

# Weekday() returns an integer from 0 to 6 for Monday to Sunday for the days of the week.
# Need an if statement to print the required output.

if today < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yah!")

# Alternative method 
# isocalendar()  Isocalendar() in date class returns a tuple containing an ISO year, week number and weekday number. 
# ISO stands for International Organization for Standardization
# Week starts on Monday, with Monday equal to 1 and Sunday equal to 7.
# As the weekday number is at index 2, we use bracket notation to access the weekday part of isocalendar().

week_day = date.today().isocalendar()[2]

if week_day == 6 or week_day == 7:
    print("It is the weekend, yah!")
else:
    print("Yes, unfortunately today is a weekday.")


'''References:
https://www.analyticsvidhya.com/blog/2020/05/datetime-variables-python-pandas/

https://ioflood.com/blog/python-get-current-date/

https://www.dataquest.io/blog/python-datetime/

'''