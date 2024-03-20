# bank.py
# Prompt the user and read in two money amounts in cents
# Add the two amounts
# Print the answer in euro and cents €0.00
# Author: Irene Kilgannon

# Enter the first amount
amount1 = int(input('Enter amount1 (in cent): '))

# Enter the second amount
amount2 = int(input('Enter amount2 (in cent): '))

# If (amount1 + amount2)/100 were used to calculate €0.00, there could potentially be floating point errors.

# A better method would use floor division (//) and modulo (%).

# // floor division gives the euro amount rounded down to the nearest whole number.
euro = (amount1 + amount2) // 100

# % gives the remainder to calculate the cent amount. 
cent = (amount1 + amount2) % 100

# Print the required output in €euro.cent
print(f'The sum of these is €{euro}.{cent}')


'''References:
Floating point errors: https://docs.python.org/3/tutorial/floatingpoint.html
FLoor division: (https://www.geeksforgeeks.org/floor-division-in-python/)
Modulo: https://realpython.com/python-modulo-operator/#modulo-operator-with-float

'''