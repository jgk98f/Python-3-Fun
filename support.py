#!/usr/bin/python3

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: A set of useful functions to support python development.
##
import time

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Get human readable time and return it.
##
def getCurrentTime():
	currentTime = time.asctime(time.localtime(time.time()))
	return currentTime

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