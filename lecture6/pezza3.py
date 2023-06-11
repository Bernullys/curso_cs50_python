import sys
from tabulate import tabulate
import csv

def main():
    check_input()
    menu = []
    try:
        with open(sys.argv[1]) as csv_menu:
            reader = csv.reader(csv_menu)
            for row in reader:
                menu.append(row)
            print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")

def check_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

if __name__=="__main__":
    main()