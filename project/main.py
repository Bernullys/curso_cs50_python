import sys
import time
import csv
from bill import Bill

options = {
    "Show the menu": 1,
    "Initialize a bill": 2,
    #Every time a customer has initialized, the app should keep track with a respald of its bill in a csv file.
    #So in a csv file named current_bills.csv will be create an ID and the name of each customer.
    "Check active customers": 3,
    "Print the bill by customer": 4,
    "Add item to an active customer": 5,
    "Confirm paiment and Save bill in a pdf into a different folder": 6, #Once a bill has been paid, the customer must be take out of the custumers list, and their items out of current_bills.csv. Also create a pdf with a invoice.
    "Add a new product to the menu": 7,
    "Delete a product from the menu": 8,
    "Show stock": 9,
    "Add or Delete stock": 10,
    "Change the price of a product": 11,
    "Check today's sell": 12,
    "Quit": 13,
    #Would be cool if I can check the amount in bitcoins currency
}

def main():
    
    #in this list we will store all the coustumers bill stancies.
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
        elif  selected_option == "3":   #This option prints the lenght of the list of custumers and then sweep the list to show each customer with its index.
            print(f"Now we have {len(custumers)} actives. Those are:")
            for index, c in enumerate(custumers):
                print(f"Custumer {index + 1}: {c.custumer_name}")

        elif selected_option == "4":    #This option ask for the customer name and then it shows the bill of that customer
            check_custumer = input("Custumer name: ")
            for custumer in custumers:
                if custumer.custumer_name == check_custumer:
                    custumer.tap(10)
        
        elif selected_option == "5":    #This option is to add item(s) to an existin customer's bill. 
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