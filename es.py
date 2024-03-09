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


import sys

if len(sys.argv) != 2:
    print('Error: missing argument')
    sys.exit(1)


# File name does not exist, check file type. HOw?

# Not a txt file
    

# Output when running: python3 your_script.py
# Error: missing argument

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    e_cont = f.read().count('e')
    #E_cont = f.read().count('E')

print(e_cont)