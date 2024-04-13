# Write a program that outputs whether or not today is a weekday
# If it is a weekday output is "Yes, unfortunately today is a weekday".
# If weekend output "It is the weekend, yah!"
# Author: Irene Kilgannon


# Import the date class from the datetime module
from datetime import date

# To find today's date, use the built in today() method.
# Use weekday() of class date in the datetime module to extract the day of the week. 
today = date.today().weekday()


# Weekday() returns an integer from 0 to 6 for Monday to Sunday for the days of the week.

# Need an if statement to print the required output depending on the result of the today variable
# Less than 5 is any day before Saturday. The integer 5 corresponds to Saturday.
if today < 5:
    print("Yes, unfortunately today is a weekday.")

# If weekday() returns 5 or 6, i.e. Saturday or Sunday it will print the following:
else:
    print("It is the weekend, yah!")


# See weekday.ipynb for additional comments and references (https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/weekday.ipynb)