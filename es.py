# Write a program that reads in a text file
# Outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author Irene Kilgannon

import os
import sys

# Check the number of arguments in sys.argv
if len(sys.argv) != 2:
        print(f"Error: One file is required, {len(sys.argv)-1} were given")
        sys.exit(1)

# 
file_name = sys.argv[1]

# Check the file extension. Must be .txt
root, ext = os.path.splitext(file_name)            # os.path.splitext() splits the file name by the last dot on the right into the root and the ext
if ext != ".txt":
    print(f"Error: File format must be .txt. File format given was {ext}.")
    sys.exit(1)

# Open the file to read it.
try:
    with open(file_name, 'r') as f:
        e_count = f.read().lower().count("e")     # To count all the e's, change the capital letters to lowercase with .lower(), then use .count() to count the e's. 
        print(e_count)                            # Print the result.

except FileNotFoundError:                         # Print an exception if the file was not found. 
    print("That file was not found")  


# https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
# https://www.youtube.com/watch?v=LpZmZs2_BC4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=39