# bank.py
# A program that reads in a 10 character account number.
# Outputs the account number with only the last 4 digits showing and the first 6 replaced with X's.
# Author: Irene Kilgannon


# Ask the user to input a ten digit account number. 
account = str(input("Please enter a 10 digit account number: ")) 

# Check length of the account number
if len(account) != 10:
    print("Error, only 10 digits allowed.")

# The following will run if the length of the account number is equal to 10
else:
    # String.replace(old value, new value) 
    # Old value is the string up to the last four digits.
    # New value is the length of the string multiplied by "X"
    hidden_account = account.replace(account[:-4], len(account[:-4]) * "X")

    # Print the new_account number with the first 6 numbers replaced with X's.
    print(hidden_account)


# Modify program to deal with a/c of any length.
# Assume the a/c number is at least 5 digits in length so that we have at least 1 number along with 4 X's.

# Input
any_account = str(input("Please enter an account number: "))

# Check the length of any_account_length
if len(any_account) < 5:
    print("At least 5 digits are required.")

# String replace method as used above.
else:
    print(any_account.replace(any_account[:-4], len(any_account[:-4]) * "X"))



# Link to the associated jupyter notebook: https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/accounts.ipynb
