# bank.py
# A program that reads in a 10 character account number
# Outputs the account number with only the last 4 digits showing and the first 6 replaced with X's
# Author: Irene Kilgannon

#Thoughts a/c no's are strings, how do I limit to 10 digits? Check length. Can I separate a string into parts? YES Need to convert to list? 
#splice at [:-5]
# replace [:6]?? 
#Other idea spilt the account number, turn 1-6 into X, then merge the 2 bits back together??

account = str(input("Please enter a 10 digit account number: "))

if len(account) != 10:
    print("Error, only 10 digits allowed.")
else:
    #first_six = list(account[:6])  # as a string is immutable, change the string to a list
    #first_six[0:7] = ["XXXXXX"]  # change the list back to a string removing ,
    last_four = account[-4:]
    #re_merge = str(account).strip() # replaces first digits with 1 X, need 6 X 
    #replace = account.replace("7", "X")
    #print(first_six)
    print(last_four)
    new_account = 'XXXXXX' + last_four # https://realpython.com/python-strings/ section on modifying strings accessed 06/02/2024
    print(new_account)



#Extra: modify program to deal with a/c of any length. What assumptions do I need to make? Assume at least 4 characters? 

