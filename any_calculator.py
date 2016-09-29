"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from any_arithmetic import *


# Your code goes here
while True:
    input_string = raw_input()
    if input_string == "q":
        break
    else:
        tokens = input_string.split(" ")
        numbers = map(int, tokens[1:])

        if tokens[0] == "+":
            print add(*numbers)
        elif tokens[0] == "-":
            print subtract(*numbers)
        elif tokens[0] == "*":
            print multiply(*numbers)
        elif tokens[0] == "/":
            print divide(*numbers)
        elif tokens[0] == "square":
            print square(numbers[0])
        elif tokens[0] == "cube":
            print cube(numbers[0])
        elif tokens[0] == "pow":
            print power(*numbers)
        elif tokens[0] == "mod": 
            print mod(numbers[0], numbers[1])
        else:
            print "Sorry this is not a valid command."
        

    
      
        


