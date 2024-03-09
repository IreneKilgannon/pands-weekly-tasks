# Write a program that reads in a text file
# Outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author Irene Kilgannon



# How would I count the occurrences of a specific character in a string?

#counting = input("Enter a string: ")

'''
def counting(e):
    count = 0
    for item in data:
      if item == 'e':
         count +=1
    return count

#Find moby dick online
#https://courses.cs.washington.edu/courses/cse390c/22sp/lectures/moby.txt

with open("moby-dick.txt", 'r') as f:
   data = f.read()
   print(counting(data))'''

import os
import sys

if len(sys.argv) != 2:
    print('Error: missing argument')
    sys.exit(1)

file_name = sys.argv[1]
#https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
for fp in file_name:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(file_name)

    file_extension = ext[1]

    # Now we can simply use == to check for equality, no need for wildcards.
    if file_extension != '.txt':
        print("File format must be .txt") 
# Not a txt file, check file type. How?

file_name = sys.argv[1]
try:
    with open(file_name, 'r') as f:
        e_cont = f.read().count("e")
        print(e_cont)

# File name does not exist
# # https://www.youtube.com/watch?v=LpZmZs2_BC4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=39
except FileNotFoundError:
    print("That file was not found")



# Doesn't work
'''for file in sys.argv[1]:
    if file.endswith(".txt"):
        with open(file_name, 'r') as f:
            e_cont = f.read().count("e")
    else:
        print("Error, not a txt file")'''