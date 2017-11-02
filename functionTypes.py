#!/usr/bin/python3

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Program to play with the different kinds of function calls in Python 3.
##

##
#  Function Definitions
##

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to do standard summing of three arguements.
##
def regularSum(x, y, z):
	return x + y + z

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to do vartuple sum where 1 is the min number of arguements.
##
def doVartupleSum( x, *vartuple):

	total = x

	if( vartuple ):
		for num in vartuple:
			total += num
		return total
	else:
		return total

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to return a sum of 3 arguements using lambda function.
##
lambdaSum = lambda x, y, z: x + y + z 

#Our numbers to use
tuple = (5,10,15)

#Code to call our functions and do som summation!
print("Our numbers for the following operations will be:", tuple)

print("The multi sum is:" , doVartupleSum(5 , 10, 15))

print("The sum of one number is:", doVartupleSum(5))

print("The sum using lambda is:" , lambdaSum(5, 10, 15))

print("The sum using the regular method is:", regularSum(5, 10, 15))