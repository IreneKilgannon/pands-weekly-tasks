# bank.py
# prompt the user and read in two money amounts in cents
# add the two amounts
# print the answer in euro and cents €.00
# Author: Irene Kilgannon

#Enter the first amount
amount1 = int(input('Enter amount1 (in cent): '))

#Enter the second amount
amount2 = int(input('Enter amount2 (in cent): '))

#Add amount1 and amount2, divide by 100 to get a decimal point
money = (amount1 + amount2)/100

print(f'The sum of these is €{money:.2f}')
print('\u20ac')
#Need to have 2 decimal places in the print out. This is done by the .2f, rounds to two decimal places. 
#Insert euro symbol, return a money amount. in eurp symbol on laptop! Copy and pasted the euro symbol. Other methods
# \u20ac codes for a euro symbol


# https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python
