#This program expects one command-line argument (the name of the python file under test)

import sys

#Less than one command-line argument should say: Too few command line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
#More than one command-line argument should say: Too many command line arguments
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
#If the file under test does not ends with .py should say: Not a python file
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

lines = []

#If the file under test does not exist - should say: File does not exist
#Exclude comments
#Exclude blank lines

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.startswith("#") or line.rstrip() == "":
                lines = lines
            else:
                lines.append(line.rstrip())
except FileNotFoundError:
    print("File does not exist")

else:
    print(len(lines))

#Output the number of lines of code of the python file under test