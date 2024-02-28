import sys
import time
import csv
from bill import Bill, show_menu

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
    "Check today's sell": 11,
    "Quit": 12
}

def main():
    
    custumers = []
    n = 0
    
    presentation()

    while True:
        selected_option = selection()
        if selected_option == "1":
            show_menu("menu.csv")
        elif selected_option == "2":
            n += 1
            custumer_name = input("Custumer name: ")
            custumers.append(Bill(custumer_name))
            is_ordering = "yes"
            while is_ordering == "yes":
                custumers[n-1].order(input("First order: "))
                is_ordering = input(f" Do you want another item? ")
        elif selected_option == "3":
            check_custumer = input("Custumer name: ")
            for custumer in custumers:
                if custumer.custumer_name == check_custumer:
                    custumer.tap(10, 10)



def presentation():  
    print("Welcome to the Bar Restaurant")
    for o in options:
       time.sleep(0.1)
       print(f"Select option: {options[o]} {o}")

def selection():
    time.sleep(0.5)
    print("Select your option number")
    return input("")



if __name__== "__main__":
  main()