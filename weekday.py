# Write a program that outputs whether or not today is a weekday
# If it is a weekday output is "Yes, unfortunately today is a weekday".
# If weekend output "It is the weekend, yah!"
# Author: Irene Kilgannon

'''https://ioflood.com/blog/python-get-current-date/
Python has a datetime module that can be used to get the date
Use today = day.today() to get the current date.
Can this be used to get they day of the week?

Calendar module has a weekday() method. 
https://www.w3resource.com/python/module/calendar/weekday.php

'''

from datetime import date

import calendar

today = date.today()

print(today)

# Weekday() requires the date to be formatted as YYYY, MM, DD
# Today gives the result as YYYY-MM-DD
# Reformat the today variable
# format_date = today.strftime(%Y %m %d)

format_date = today.strftime("%Y, %m, %d")

print(format_date)

day = calendar.weekday(format_date)

# Weekday() method returns an integer 0-6 for Monday to Sunday for the day of the week.
#Need to make an if statement to print the required output.

if day == 5 or day == 6:
    print("It is the weekend, yah!")
else:
    print("Yes, unfortunately today is a weekday.")
print(day)