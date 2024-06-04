import time
import csv
from bill import Bill

options = {
    "Show the menu": 1,     # This option will call a function that will open a csv_menu.csv file wich has the current menu.
                            # Then this same function will stored it in a list and then print it in the terminal. 
                            # (The idea is to put son style in this print)
    "Initialize a bill": 2, # Every time a customer has initialized, the app should keep track with a respald of its bill in a csv file.
                            # So in a csv file named current_bills.csv will be create an ID and the name of each customer.
    "Check active customers": 3,    # This option prints the lenght of the list of custumers and then sweep the list to show each customer
                                    # with its index.
    "Check the bill by customer": 4,# This option ask for the customer name and then it shows the bill of that customer.
    "Add item to an active customer": 5,    # This option is to add an item to an existin customer's bill. 
    "Confirm paiment and save bill in a pdf into a different folder": 6,    # Once a costumer wants to pay, this option will print a the 
                                                                            # customer invoice as a pdf. (Would be good if is saved in a folder)
                                                                            # Now the costumer and its orders must be take out
                                                                            # of the custumers list, and their items out of current_bills.csv. 
    "Add a new product to the menu": 7,
    "Delete a product from the menu": 8,
    "Show stock": 9,
    "Add or Delete stock": 10,
    "Change the price of a product": 11,
    "Check today's sell": 12,
    "Quit": 13,
    # Would be cool if I can check the amount in bitcoins currency
}

def main():
    
    custumers = []  # In this list we will store all the coustumers bill stancies.
    n = 0           # n is to initialized the index of costumer in the list costumers. 
                    # So each time a costumer is added don't overlap the previews one.
    presentation()  # Presentation function is used to run the program. Presentention prints all the options the program has.

    #this while loop keep the program runing.
    while True:
        selected_option = selection()   #selection function take and return the number of the selected option.
        
        if selected_option == "1":      #show_menu function prints the menu. So the user can indicate which item wants.
            show_menu("menu.csv")       #The funtion gets as parameter the file directly.

        elif selected_option == "2":    # add a custumer. That by creating a new instance of a Bill class and is append to the list custumers.
            n += 1
            custumer_name = input("Please type the custumer name: ")
            custumers.append(Bill(custumer_name))
            is_ordering = "yes"
            while is_ordering == "yes":
                custumers[n-1].order(input(f"Please {custumer_name} tell us your order: "))
                is_ordering = input(f"{custumer_name} do you want another item? ")

        elif  selected_option == "3":   
            print(f"Now we have {len(custumers)} active(s). Those are:")
            for index, c in enumerate(custumers):   # To achive this I'm usinng enumerate build in function. (Whatch for documentation)
                print(f"Custumer {index + 1}.- {c.custumer_name}")

        elif selected_option == "4":    # This option is checking for the exact name of the costumer and the check in the Bills class the instance
                                        # which match that name. That method by default prints the bill in the terminal.
                                        # Then we are passing a 10% of taxes directly to the total amount.
            check_custumer = input("Please type the costumer name: ")
            for custumer in custumers:
                if custumer.custumer_name == check_custumer:
                    custumer.tap(10)
        
        elif selected_option == "5":    # First of all we check if the costumer exist.
                                        # Then we check for the index and the name of the costumer, so then we can add an order to the index
                                        # of that intance of the costumers list
            check_existing_custumer = input("Which custumer do you want to add an item? ")
            for i, c in enumerate(custumers): 
                if c.custumer_name == check_existing_custumer:
                    is_ordering_again = "yes"
                    while is_ordering_again == "yes":   # (Use a list with all the options to be a yes answerd).
                        custumers[i].order(input(f"{c.custumer_name} please tell us your new order: "))
                        is_ordering_again = input(f"{c.custumer_name} do you want another item? ")

        elif selected_option == "6":
            check_custumer = input("Please type the costumer which is going to pay its tap: ")
            for c in custumers:
                if c.custumer_name == check_custumer:
                    c.invoice(check_custumer)

def presentation(): # This function will print all options every time the application get started.
                    # With a time of delay so it can be aesy to read.
    print("Welcome to the __BADR__ Bar Restaurant")
    for o in options:
       time.sleep(0.01)
       print(f"Select option: {options[o]} {o}")

def selection():
    time.sleep(0.05)
    print("Select your option number")
    return input("")

def show_menu(csv_file):                                    # Here we get the menu as parameter.
   menu = []                                                # We read the file and then append it to a list.
   with open (csv_file) as csv_menu:                        # Finally we print the items and price in the terminal.
    reader = csv.reader(csv_menu)
    for row in reader:
        menu.append({"item": row[0], "price": row[1]})
    for m in menu:
       print(f"{m['item']}  {m['price']}")

if __name__== "__main__":
  main()