#!/usr/bin/python3

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Simple time program to utilize some of the time module for fun and learning purposes.
##

import time
import calendar

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Print welcome for our users.
##
def sayHello():
	print ("\nWelcome to a simple Python 3 time program!")

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Get human readable time and return it.
##
def getCurrentTime():
	currentTime = time.asctime(time.localtime(time.time()))
	return currentTime

#Print our introduction
sayHello()

#Get the local time and store it for later use.
local = time.localtime()

#Print the current human readable time.
getCurrentTime()

#Get the current calendar month dynamically and display it.
cal = calendar.month(local.tm_year, local.tm_mon)
print("\n", cal)

#Get and print the calendar for the current year.
calCurrentYear = calendar.calendar(local.tm_year, 1, 1, 1)
print("\n", calCurrentYear)

#Test to see if it is a leap year or not.
isLeap = calendar.isleap(local.tm_year)

#If it is a leap year then print appropriate message.
if( isLeap ):
	print(local.tm_year, end=" ")
	print("is a leap year!")
else:
	print(local.tm_year, end=" ")
	print("is not a leap year!")

#Cleaning up environment.
del cal, local, calCurrentYear, isLeap