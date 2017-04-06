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
                    if len(input_string) < 3:
                        print "I don't understand"
                    else:
                        print add(input_string[1:])
            elif input_string[0] == "-":
                    if len(input_string) < 3:
                        print "I don't understand"
                    else:
                        print subtract(input_string[1:])
            elif input_string[0] == "*":
                    if len(input_string) < 3:
                        print "I don't understand"
                    else:
                        print multiply(input_string[1:])
            elif input_string[0] == "/":
                if len(input_string) > 3:
                    print "Too many inputs :("
                else:
                    print divide(int(input_string[1]), int(input_string[2]))
            elif input_string[0] == "square":
                if len(input_string) > 2:
                    print "Too many inputs :("
                else:
                    print square(int(input_string[1]))
            elif input_string[0] == "cube":
                if len(input_string) > 2:
                    print "Too many inputs"
                else:
                    print cube(int(input_string[1]))
            elif input_string[0] == "pow":
                if len(input_string) > 3:
                    print "Too many inputs"
                else:
                    print power(int(input_string[1]), int(input_string[2]))
            elif input_string[0] == "mod":
                if len(input_string) > 3:
                    print "Too many inputs"
                else:
                    print mod(int(input_string[1]), int(input_string[2]))
            else:
                print "I do not understand."
        except:
            print "I do not understand"
