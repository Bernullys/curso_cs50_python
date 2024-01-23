import sys
import time
import csv
from bill import Bill

options = {
    "Show the menu": 1,
    "Initialize a bill": 2,
    "Print the bill by customer": 3,
    "Confirm paiment": 4,
    "Save bill in pdf": 5,
    "Add a new product to the menu": 6,
    "Delete a product from the menu": 7,
    "Show stock": 8,
    "Add stock": 9,
    "Change the price of a product": 10,
    "Check today's sell": 11
}

def main():
    
    presentation()
    selected_option = selection()

    if selected_option == "1":
       show_menu()


def presentation():
    print("Welcome to the Bar Restaurant")
    for o in options:
       time.sleep(0.5)
       print(f"Select option: {options[o]} {o}")

def selection():
    time.sleep(0.5)
    print("Select your number option")
    return input("")

def show_menu():
   menu = []
   with open ("menu.csv") as csv_menu:
    reader = csv.reader(csv_menu)
    for row in reader:
        menu.append({"item": row[0], "price": row[1]})
    for m in menu:
       print(f"{m['item']} Price:{m['price']}")


if __name__== "__main__":
  main()