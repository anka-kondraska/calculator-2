"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
	input_string = raw_input()
	tokens = input_string.split(" ")
	while len(tokens) < 3:
		tokens.append(0)
	num1 = int(tokens[1])
	num2 = int(tokens[2])
	if tokens[0] == "q":
		break
	elif tokens[0] == "+":
		print add(num1, num2)
	elif tokens[0] == "-":
		print subtract(num1, num2)
	elif tokens[0] == "*":
		print multiply(num1, num2)
	elif tokens[0] == "/":
		print divide(num1, num2)
	elif tokens[0] == "square":
		print square(num1)
	elif tokens[0] == "cube":
		print cube(num1)
	elif tokens[0] == "pow":
		print power(num1, num2)
	elif tokens[0] == "mod":
		print mod(num1, num2)
	else:
		print "Sorry this is not a valid command."
		break


