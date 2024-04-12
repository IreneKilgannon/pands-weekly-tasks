# bank.py
# Prompt the user and read in two money amounts in cents
# Add the two amounts
# Print the answer in euro and cents €0.00
# Author: Irene Kilgannon

# Error handling to ensure amount entered is a whole number.
try:
    # Enter the first amount
    amount1 = int(input('Enter amount1 (in cent): '))

    # Enter the second amount
    amount2 = int(input('Enter amount2 (in cent): '))

# If (amount1 + amount2)/100 was used to calculate the total amount, this could result in floating point errors.

# A better method would use floor division (//) and modulo (%).

    # // floor division gives the euro amount rounded down to the nearest whole number.
    euro = (amount1 + amount2) // 100

    # % gives the remainder to calculate the cent amount. 
    cent = (amount1 + amount2) % 100

    # Print the required output in €euro.cent
    print(f'The sum of these is €{euro}.{cent}')

# The error message will print if an integer is not entered.
except ValueError:
    print('Error: The amount entered must be a whole number.')