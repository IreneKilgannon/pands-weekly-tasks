# bank.py
# prompt the user and read in two money amounts in cents
# add the two amounts
# print the answer in euro and cents €.00
# Author: Irene Kilgannon

# Enter the first amount
amount1 = int(input('Enter amount1 (in cent): '))

# Enter the second amount
amount2 = int(input('Enter amount2 (in cent): '))

# If we use (amount1 and amount2)/100, we could potentially get floating point errors.

# A better method uses floor division and %.
# // floor division gives the euro amount rounded down to the nearest whole number.
euro = (amount1 + amount2) // 100

# % gives the remainder to calculate the cents. 
cent = (amount1 + amount2) % 100

# Print the required output in €euro.cent
print(f'The sum of these is €{euro}.{cent}')

'''References:
Floating point errors: https://docs.python.org/3/tutorial/floatingpoint.html

'''