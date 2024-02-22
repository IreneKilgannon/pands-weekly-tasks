# bank.py
# A program that reads in a 10 character account number
# Outputs the account number with only the last 4 digits showing and the first 6 replaced with X's
# Author: Irene Kilgannon

#Thoughts a/c no's are strings, how do I limit to 10 digits? Check length. Can I separate a string into parts? YES
#Other idea spilt the account number, turn 1-6 into X, then merge the 2 bits back together??

account = str(input("Please enter a 10 digit account number: "))

if len(account) != 10:
    print("Error, only 10 digits allowed.")
else:
    first_six = account[0:6]
    last_four = account[-4:]
    print(last_four)
    new_account = 'XXXXXX' + last_four # https://realpython.com/python-strings/ section on modifying strings accessed 06/02/2024
    print(new_account)

first_sixnew = account[0:6]
X_file = (len(first_sixnew)) * "X"
print(X_file + last_four) 

#Extra: modify program to deal with a/c of any length. What assumptions do I need to make? Assume at least 4 characters? 

extra_account = str(input("Please enter an account number: "))

first_sixnew2 = extra_account[:-4]
print(first_sixnew2)
last_four2 = extra_account[-4:]
print(last_four2)

# Use the 
X_file2 = (len(first_sixnew2)) * "X"
print(X_file2 + last_four2) 
