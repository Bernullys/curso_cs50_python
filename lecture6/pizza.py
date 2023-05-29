#the program expects one command-line argument of a csv file

#more than one command-line --- Too many command-line arguments
#less than one command-line -- Too few command-line arguments
#not a csv file -- Not a CSV file
#if the specified file does not exist -- That file does not exist
import csv
import sys
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

menu = []
try:
    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile)
        for menu_line in reader:
            menu.append(menu_line)
except FileNotFoundError:
    print("File does not exist")

#outputs a table with ASCII format

print(tabulate(menu, headers="firstrow", tablefmt="grid"))