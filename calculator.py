"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# No setup
# repeat forever:
while True:
    # read input
    input = raw_input("> ")
    # tokenize input
    input_string = input.split(" ")
    # if the first token is "q":
    if input_string[0] == "q":
        # quit
        break
    # else:
    else:
        try:
            # decide which math function to call based on first token
            if input_string[0] == "+":
                    print add(input_string[1:])
            elif input_string[0] == "-":
                    print subtract(input_string[1:])
            elif input_string[0] == "*":
                print multiply(int(input_string[1]), int(input_string[2]))
            elif input_string[0] == "/":
                print divide(int(input_string[1]), int(input_string[2]))
            elif input_string[0] == "square":
                print square(int(input_string[1]))
            elif input_string[0] == "cube":
                print cube(int(input_string[1]))
            elif input_string[0] == "pow":
                print power(int(input_string[1]), int(input_string[2]))
            elif input_string[0] == "mod":
                print mod(int(input_string[1]), int(input_string[2]))
            else:
                print "I do not understand."
        except ValueError:
            print "I do not understand"
