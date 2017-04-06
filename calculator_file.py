"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.

Takes inputs from file and outputs to the same file
"""

from arithmetic import *

math_data = open("math.txt")

# Your code goes here
# No setup
# Iterates through each line of the text file:
for calc in math_data:
    # Splits each line of text in file into a list of its parts
    input_string = calc.split(" ")

    try:
        # decide which math function to call based on first token
        if input_string[0] == "+":
                if len(input_string) < 3:
                    print "I don't understand"
                else:
                    print add_list(input_string[1:])
        elif input_string[0] == "-":
                if len(input_string) < 3:
                    print "I don't understand"
                else:
                    print subtract_list(input_string[1:])
        elif input_string[0] == "*":
                if len(input_string) < 3:
                    print "I don't understand"
                else:
                    print multiply_list(input_string[1:])
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
        elif input_string[0] == "x+":
            if len(input_string) > 4:
                print "Too many inputs"
            else:
                print add_mult(int(input_string[1]), int(input_string[2]), int(input_string[3]))
        elif input_string[0] == "cubes+":
            if len(input_string) > 3:
                print "Too many inputs"
            else:
                print add_cubes(int(input_string[1]), int(input_string[2]))
        else:
            print "I do not understand."
    except:
        print "I do not understand"
