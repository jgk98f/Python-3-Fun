#!/usr/bin/python3

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Define a python function that does fizzbuzz for a random number. This will be imported in "modules.py". The only thing taken from this will be function fizzbuzz.
##

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to perform the fizzbuzz game.
##
def fizzbuzz(x):

	if( x % 15 == 0 ):
		print("fizzbuzz")
	elif( x % 10 == 0 ):
		print("fizz")
	elif(x % 5 == 0 ):
		print("buzz")
	else:
		print("Number is not mod 5, 10, or both 5 and 10!")
