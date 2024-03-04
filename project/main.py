import sys
import time
import csv
from bill import Bill

options = {
    "Show the menu": 1,
    "Initialize a bill": 2,
    "Check active customers": 3,
    "Print the bill by customer": 4,
    "Add item to an active customer": 5,
    "Confirm paiment": 5,
    "Save bill in pdf": 6,
    "Add a new product to the menu": 7,
    "Delete a product from the menu": 8,
    "Show stock": 9,
    "Add stock": 10,
    "Change the price of a product": 11,
    "Check today's sell": 12,
    "Quit": 13
}

def main():
    
    #in this list we will store all the coustumers bill.
    custumers = []
    n = 0   #n is to initial
    
    #presentation function is used to run the program. Presentention prints all the options the program has.
    presentation()

    #this while loop keep the program runing.
    while True:
        selected_option = selection()   #selection function take and return the number of the selected option.
        if selected_option == "1":      #show_menu function prints the menu. So the user can indicate with item wants.
            show_menu("menu.csv")       
        elif selected_option == "2":    # add a custumer. That by creating a new instance of a Bill class and is append to the list of custumers.
            n += 1
            custumer_name = input("Custumer name: ")
            custumers.append(Bill(custumer_name))
            is_ordering = "yes"
            while is_ordering == "yes":
                custumers[n-1].order(input(f"{custumer_name} tell us your order: "))
                is_ordering = input(f"{custumer_name} Do you want another item? ")
        elif  selected_option == "3":
            print(f"Now we have {len(custumers)} actives. Those are:")
            for index, c in enumerate(custumers):
                print(f"Custumer {index + 1}: {c.custumer_name}")

        elif selected_option == "4":
            check_custumer = input("Custumer name: ")
            for custumer in custumers:
                if custumer.custumer_name == check_custumer:
                    custumer.tap(10)
        
        elif selected_option == "5":
            check_existing_custumer = input("Which custumer do you want to add an item? ")
            for i, c in enumerate(custumers):
                if c.custumer_name == check_existing_custumer:
                    is_ordering_again = "yes"
                    while is_ordering_again == "yes":
                        custumers[i].order(input(f"{c.custumer_name} tell us your new order: "))
                        is_ordering_again = input(f"{c.custumer_name} do you want another item? ")


def presentation():  
    print("Welcome to the Bar Restaurant")
    for o in options:
       time.sleep(0.01)
       print(f"Select option: {options[o]} {o}")

def selection():
    time.sleep(0.05)
    print("Select your option number")
    return input("")

def show_menu(csv_file):
   menu = []
   with open (csv_file) as csv_menu:
    reader = csv.reader(csv_menu)
    for row in reader:
        menu.append({"item": row[0], "price": row[1]})
    for m in menu:
       print(f"{m['item']}  {m['price']}")

if __name__== "__main__":
  main()