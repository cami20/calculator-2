# def add(num1, num2):
#     """Return the sum of two numbers"""
#     return num1 + num2

def add(num):
    """Return the sum of a list of numbers"""
    total = 0
    for number in num:
        total += int(number)
    return total

# def subtract(num1, num2):
#     """Return the difference of two numbers"""
#     return num1 - num2

def subtract(num):
    """Return the difference of a list of numbers"""
    total = int(num[0]) * 2
    for number in num:
        total -= int(number)
    return total


# def multiply(num1, num2):
#     """Return the product of two numbers"""
#     return num1 * num2

def multiply(num):
    """Return the product of a list of numbers"""
    total = 1
    for number in num:
        total *= int(number)
    return total


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / num2


def square(num):
    """Return the square of a number"""
    return num * num


def cube(num):
    """Return the cube of a number"""
    return num ** 3


def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num ** exponent


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2


# def add_mult(num1, num2, num3):
#     """Return sum of the first two numbers multiplied by third number"""
#     return (num1 + num2) * num3

# print add_mult(1, 2, 3)    


# def add_cubes(num1, num2):
#     """Return sum of cube of both numbers"""
#     return (num1 ** 3) + (num2 ** 3)

# print add_cubes(2, 3)