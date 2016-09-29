def add(*args):
    """ Returns the sum of two numbers """
    return sum(args)


def subtract(*args):
    """ Returns the difference of the second argument from the first argument """
    difference = args[0]
    for i in args[1:]:
        difference -= i
    return difference


def multiply(*args):
    """ Returns the product of two numbers """
    multi = args[0]
    for i in args[1:]:
        multi *= i
    return multi


def divide(*args):
    """ Returns the floating point quotient of the first argument divided by the second """
    dive = float(args[0])
    for i in args[1:]:
        dive /= i
    return dive


def square(num1):
    """ Returns the square of the argument """

    return num1 * num1


def cube(num1):
    """ Returns the cube of the argument """

    return num1 * num1 * num1


def power(*args):
    """ Returns the result of raising the first input to the power of the second input """
    powpow = args[0]
    for i in args[1:]:
        powpow **= i
    return powpow


def mod(num1, num2):
    """ Returns the remainder when the first input is divided by the second input """

    return num1 % num2
