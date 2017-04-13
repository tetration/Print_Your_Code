#PrintYourCode Linux version python 2.x
#Github author address: https://github.com/tetration
#Contact: Tetration@outlook.com
#Written for Python 2.x and 3.x
#Warning This version is for Python 2 Only!
import os
import subprocess
import fnmatch

name=''
def AskforName():
	print("Type the name of the file (Dont forget to type the extension as well)")
	print("Example: test.cpp")
	print("Warning: names with spaces might not work very well.")
	name=raw_input()
	AskforDirectory(name)

def AskforDirectory(name):
	user=''
	print("Where is it located at?")
	print("Type 1: Same Directory as this python script")
	print("Type 2: Type the directory")
	user=str(raw_input())
	filedir=('')
	if user==('1'):
		filedir=('')
		VimDirectoryGoer(name,filedir)
	
	if user==('2'):
		print("Please type the directory then")
		print("Example: /home/YourUsername/Desktop/Folder_with_your_Code")
		filedir=raw_input()
		VimDirectoryGoer(name,filedir)

	else :
		print("Please type 1 or 2 and then press enter")
		AskforDirectory()

def VimDirectoryGoer(name, filedir):
	if filedir!='':
		#seq=('cd ',filedir)
		#os.system(''.join(seq))
		os.chdir(filedir)

	CheckforFile(name,filedir)
	VimPrinter()

def CheckforFile(name,filedir):# Checks if it can find a file with the same name given by the user in this directory
	print("Checking if file exists...")
	if os.path.isfile(name)==True:
    			seq=('File found! ',name," typed by the user matched:", name, " in current directory")
    			print(''.join(seq))
    			VimPrinter(name)

	elif os.path.isfile(name)==False:
    		print("File not found! Please move your code file to this directory")
    		print("or make sure you typed the right name")
    		print("This program will now restart itself...")
    		print("")
    		Fail_restart()


def VimPrinter(name):
	print("Would you like to give a different name to the file or just leave it with the same name")
	print("Type: 1 to leave as the same name")
	print("Type: 2 to create a new name")
	user=str(raw_input())
	if user=='1':
		filename=name
		
	if user=='2':
		print("What name would you like to give to your pdf file?")
		filename=raw_input()
	seq=("vim ",name," -c ",'"hardcopy > ',filename,'.pdf | q"')
	os.system(''.join(seq))
	print("Conversion to PDF completed!")
	seq=("PDF File can be found in: ",os.getcwd())
	print(''.join(seq))
	exit()
	#vim example.py -c "hardcopy > example.pdf | q"
	#Command to print directly without the help of this script

def Welcome():
	print("PrintYourCode for Linux written in Python")

def Fail_restart():#Restarts the program if the user fails to type the correct directory
	main()

def main():
	Welcome()
	AskforName()

#Initializer
main()

