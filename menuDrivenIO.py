#!/usr/bin/python3

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Play around with menu and IO. Import OS for directory access and file deletion. We will only be using this for file deletion and file renaming.
##
import os

##
#  Functions
##

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to read data from a file and output to stdout.
##
def readFromFile():
	fileName = input("Enter the name of the file that you wish to read from.\n")

	try:
		fo = open(fileName, 'r', 256)
		print("File: " + fileName + " has been successfully opened.\n")
		fileContents = fo.read()
		print(fileContents + "\n")
		fo.close()
	except IOError:
		print("\n\nError: That file does not exist in your cwd. Next time choose one that does exist.\n\n")
		return


##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to write data to a file.
##
def writeToFile():
	try:
		fileName = input("Enter the name of the file that you wish to write to. \nIf it is not found then the file will be created automatically.\n")
		fo = open(fileName, 'w', 256)
		print("File: " + fileName + " has been successfully opened.")
		string = input("\nType what you want to write to file and press enter.\n")
		fo.write(string)
		print("\nClosing file " + fileName + "\n")
		fo.close()
	except IOError:
		print("\n\nError: " + fileName + " could not be opened on the system. Check with your admin and try again later.\n\n")
		return

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to delete a file on the system.
##
def deleteFile():
	try:
		fileName = input("\nEnter the name of the file that you wish to delete.\n")
		os.remove(fileName)
		print("Update: " + fileName + " has been successfully removed!\n")
	except OSError:
		print("\n\nError: " + fileName + " could not be deleted by the os at this time.\nMake sure the file is not in use by another program.\nIf that fails, check with your system admin and try again later.\n\n")
		return

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Function to delete a file on the system.
##
def renameFile():
	try:
		fileName = input("\nEnter the name of the file that you wish to rename.\n")
		newName = input("\nEnter the new desired name for the file.\n")
		os.rename(fileName, newName)
		print("File " + fileName + " has been successfully renamed to " + newName + "!\n")
	except OSError:
		print("\n\nError: " + fileName + " could not be renamed.\nMake sure the file is not in use by another program.\nIf that fails, check with your system admin and try again later.\n\n")
		return

##
#  End of Functions Section
##

##
#  Author: Jason Klamert
#  Date: 11/1/2017
#  Purpose: Driver for the IO program.
##
def main():

	while True:
		print("You are currently in " + os.getcwd() + "!")
		print("--------------------------------------------")
		print("1) Read from a file.")
		print("2) Write to a file.")
		print("3) Delete a file.")
		print("4) Rename a file.")
		print("5) Quit the program.")
		print("--------------------------------------------")
		choice = input("\nEnter the digit of your menu option!\n")

		if( choice == '1' ):
			readFromFile()
		elif( choice == '2' ):
			writeToFile()
		elif( choice == '3' ):
			deleteFile()
		elif( choice == '4' ):
			renameFile()
		elif( choice == '5' ):
			print("\nTerminating the program!")
			exit()
		else:
			print("\nPlease enter the digit of your choice of action.\n")
			print("Here are the options again.\n")
			continue

main()