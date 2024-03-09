# Write a program that reads in a text file
# Outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author Irene Kilgannon



# How would I count the occurrences of a specific character in a string?

#counting = input("Enter a string: ")


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
   print(counting(data))



import sys

#for arg in sys.argv:
 #   print(counting(data))

count = 0

n = len(sys.argv)

for i in range(1, n):
    if i == 'e':
        count +=1
print(count)
    

for arg in sys.argv:
    with open(arg[1], 'r') as f:
       data = f.read()
       print(counting(data))