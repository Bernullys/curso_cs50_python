import sys
import time
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
    selection()


def selection():
    time.sleep(1.5)
    print("Select your number option")
    option_selected = input("")

def presentation():
    print("Welcome to the Bar Restaurant")
    for o in options:
       time.sleep(1.5)
       print(f"Select option: {options[o]} {o}")


if __name__== "__main__":
  main()