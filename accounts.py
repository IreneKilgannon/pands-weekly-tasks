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


# Modify program to deal with a/c of any length. Assume the a/c number is at least 5 digits in length.

# Input
any_account_length = str(input("Please enter an account number: "))

if len(any_account_length) < 5:
    print("At least 5 digits are required.")

else:
    # Slice the string into two parts. The first part of the string up to and not inclulding the last 4 digits.
    first_part = any_account_length[:-4]

    # Last four digits of the any_account string. 
    last_four2 = any_account_length[-4:]

    # Get the length of the first part of the account number. Multiply the length by "X".
    # This will return the correct number of X's for the length of first part of the account.
    x_account = (len(first_part)) * "X"

# Print the result of the concatenatation x_account with the last four digits
    print(x_account + last_four2)


'''References

[Python strings](https://realpython.com/python-strings/). The sections on string indexing, string slicing and modifying strings were particularily useful.

[Python string concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp)'''