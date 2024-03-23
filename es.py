# Write a program that reads in a text file
# Outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author: Irene Kilgannon

import os
import sys

# Assign a variable name to the file at sys.argv[1].
file_name = sys.argv[1]

# Split the file by the last . on the right.
root, ext = os.path.splitext(sys.argv[1])

# Open the file to read it.
try:
    with open(sys.argv[1], 'r') as f:
        # Count all the e's after converting them to lower case with lower()
        e_count = f.read().lower().count("e")
        print(e_count)

# Check that only one file name to read was entered in the command line.
except IndexError:
    print((f"Error: One file is required, {len(sys.argv)-1} were given."))

# Check that ext is .txt. If not print error message. 
except:
    if ext != ".txt":
        print(f"Error: File format must be .txt. File format given was {ext}.")

# Print an exception if the file was not found.
except FileNotFoundError:
    print("That file was not found.")  


# For more detailed comments and references check out the jupyter notebook associated with this program. https://github.com/IreneKilgannon/pands-weekly-tasks/blob/main/es.ipynb
