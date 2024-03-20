# Write a program that reads in a text file
# Outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author: Irene Kilgannon

import os
import sys

# Check the number of arguments in sys.argv
if len(sys.argv) != 2:
        print(f"Error: One file is required, {len(sys.argv)-1} were given")
        sys.exit(1)

# Assigning a variable name to the file at sys.argv[1].
file_name = sys.argv[1]

# Check the file extension. ext must be .txt
root, ext = os.path.splitext(file_name)
if ext != ".txt":
    print(f"Error: File format must be .txt. File format given was {ext}.")
    sys.exit(1)

# Open the file to read it.
try:
    with open(file_name, 'r') as f:
        # Count all the e's after converting them to lower case with lower()
        e_count = f.read().lower().count("e")
        print(e_count)

# Print an exception if the file was not found.
except FileNotFoundError:                          
    print("That file was not found")  


# For more detailed comments and references check out the jupyter notebook associated with this program. https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/es.ipynb
