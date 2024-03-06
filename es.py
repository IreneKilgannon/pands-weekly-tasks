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

# Find moby dick online
#https://courses.cs.washington.edu/courses/cse390c/22sp/lectures/moby.txt

with open("moby-dick.txt", 'r') as f:
    data = f.read()
    print(counting(data))

