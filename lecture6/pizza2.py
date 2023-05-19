#the program expects one command-line argument of a csv file
#more than one command-line --- Too many command-line arguments
#less than one command-line -- Too few command-line arguments
#not a csv file -- Not a CSV file
#if the specified file does not exist -- That file does not exist

import csv
import sys
from tabulate import tabulate
from lines2 import exact_input

exact_input()
menu = []
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)    #the reader = csv.reader() function create one list for each row of our csv file
    for menu_line in reader:        #the diffference with DictReader is that DictReader create one dictionary for each row of our csv file
        menu.append(menu_line)

print(tabulate(menu, headers="firstrow", tablefmt="grid"))