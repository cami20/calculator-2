"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# No setup
# repeat forever:
while True:
#     read input
    input = raw_input("> ")
#     tokenize input
    input_string = input.split(" ")
#     if the first token is "q":
    if input_string[0] == "q":
#         quit
        break
#     else:
    else:
#         decide which math function to call based on first token
        if input_string[0] == "+":
            print add(int(input_string[1]), int(input_string[2]))

