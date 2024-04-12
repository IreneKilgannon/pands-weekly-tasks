# bank.py
# A program that reads in a 10 character account number.
# Outputs the account number with only the last 4 digits showing and the first 6 replaced with X's.
# Author: Irene Kilgannon


# Input 
account = str(input("Please enter a 10 digit account number: ")) 

# Check length of the account number
if len(account) != 10:
    print("Error, only 10 digits allowed.")

# The following will run if the length of the account number is equal to 10
else:
    # Slice the string to get the last four digits and give the last four digits a new variable name (last_four)
    last_four = account[-4:]

    # Concatenate 'XXXXXX' with the last_four variable
    new_account = 'XXXXXX' + last_four

    # Print the new_account number with the first 6 numbers replaced with X's.
    print(new_account)


# Modify program to deal with a/c of any length.
# Assume the a/c number is at least 5 digits in length so that we have at least 1 number along with the 4 X's.

# Input
any_account_length = str(input("Please enter an account number: "))

# Check the length of any_account_length
if len(any_account_length) < 5:
    print("At least 5 digits are required.")

# Calculate the length of the account number up to the last four characters. Multiply the length by X. 
# Concatenate the result with the last four digits.
# Print the result.
else:
    print((len(any_account_length[:-4]) * "X") + any_account_length[-4:])



# Link to the associated jupyter notebook: https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/accounts.ipynb
