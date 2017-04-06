"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.

Takes inputs from file and outputs to the same file
"""

from arithmetic import *

input_file = raw_input("What file would you like to open: ")
output_file = raw_input("What file would you like to write into: ")

math_data = open(input_file)
answers_data = open(output_file, 'r+')

# Your code goes here
# No setup
# Iterates through each line of the text file:
for calc in math_data:
    # Splits each line of text in file into a list of its parts
    input_string = calc.split(" ")

   # try:
        # decide which math function to call based on first token
    if input_string[0] == "+":
            if len(input_string) < 3:
                print "I don't understand"
            else:
                num_add = str(add_list(input_string[1:]))
                answers_data.write(num_add + "\n")
    elif input_string[0] == "-":
            if len(input_string) < 3:
                print "I don't understand"
            else:
                num_substract = str(subtract_list(input_string[1:]))
                answers_data.write(num_substract + "\n")
    elif input_string[0] == "*":
            if len(input_string) < 3:
                print "I don't understand"
            else:
                num_mult = str(multiply_list(input_string[1:]))
                answers_data.write(num_mult + "\n")
    elif input_string[0] == "/":
        if len(input_string) > 3:
            print "Too many inputs :("
        else:
            num_divide = str(divide(int(input_string[1]), int(input_string[2])))
            answers_data.write(num_divide + "\n")
    elif input_string[0] == "square":
        if len(input_string) > 2:
            print "Too many inputs :("
        else:
            num_square = str(square(int(input_string[1])))
            answers_data.write(num_square + "\n")
    elif input_string[0] == "cube":
        if len(input_string) > 2:
            print "Too many inputs"
        else:
            num_cube = str(cube(int(input_string[1])))
            answers_data.write(num_cube + "\n")
    elif input_string[0] == "pow":
        if len(input_string) > 3:
            print "Too many inputs"
        else:
            num_power = str(power(int(input_string[1]), int(input_string[2])))
            answers_data.write(num_power + "\n")
    elif input_string[0] == "mod":
        if len(input_string) > 3:
            print "Too many inputs"
        else:
            num_mod = str(mod(int(input_string[1]), int(input_string[2])))
            answers_data.write(num_mod + "\n")
    elif input_string[0] == "x+":
        if len(input_string) > 4:
            print "Too many inputs"
        else:
            num_add_mult = str(add_mult(int(input_string[1]), int(input_string[2]), int(input_string[3])))
            answers_data.write(num_add_mult + "\n")
    elif input_string[0] == "cubes+":
        if len(input_string) > 3:
            print "Too many inputs"
        else:
            num_add_cubes = str(add_cubes(int(input_string[1]), int(input_string[2])))
            answers_data.write(num_add_cubes + "\n")
    else:
        print "I do not understand."
    # except:
    #    print "I do not understand"
