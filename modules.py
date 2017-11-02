#!/usr/bin/python3

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Play around with python modules.
##
import support
from fizzbuzz import fizzbuzz

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: A function to use locals() and globals() function calls.
##
def aFuntion():
	localVariable = 0
	print("\nLocal Vars:", locals())
	print("\nGlobal Vars:", globals())

#our functions from the other files should now be in scope. Thus, lets invoke them!
print("Welcome user!")
print("You have invoked the program on date:", support.getCurrentTime())
print("Using our previous sum function:" , support.regularSum(5, 10, 15))
print("Using our previous tuplesum:", support.doVartupleSum(5, 10, 15))
print("Using our previous lambda sum handler:", support.lambdaSum(5, 10, 15))
fizzbuzz(int(30))

names = dir(support)
print("\nContent in support:", names)

aFuntion()