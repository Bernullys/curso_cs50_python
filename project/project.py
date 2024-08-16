import time
import csv
import re
from tabulate import tabulate
from bill import Bill

# Options is a dict which contains all the characteristics of this project, where each key is the characteristic and its value is a number from 0 to 11 where the user can select to work when running a bar restaurant.
options = {
    "Show Options": 0,
    "Show the Menu": 1,
    "Initialize a customer": 2,
    "Check active customers": 3,
    "Check the bill for a customer": 4,
    "Add an item to an active customer": 5, 
    "Confirm payment and save the bill as a PDF": 6,
    "Add a new item to the menu": 7,
    "Remove an item from the menu": 8,
    "Show the stock levels for each item": 9,
    "Add stock to a specific item": 10,
    "Exit": 11,
}

afirm = ["yes", "y"]
customers = []  # In this list we will store all the coustumers bill instancies.
menu = "./menu.csv"

def main():

    # Presentation function is used to  welcome and show the user which are all the options the program has.
    presentation()  

    # This while loop keep the program runing.
    while True:     
        try:
            while True:
                try:
                    # Selection function will ask the user constantly for a number between 1 and 11  which take and return the number of the selected option.
                    selected_option = selection(input("Please type your option number: ").strip())
                except ValueError:
                    print("Invalid option, please try a digit between 0 and 11")
                    pass
                else:
                    break
            
            # Print the options again if needed.
            if selected_option == "0":
                presentation()

            # show_menu function prints the menu. So the user can indicate which item wants.
            elif selected_option == "1":
                listed_current_menu = open_csv_to_read("")
                show_table_in_terminal(listed_current_menu, "Item", "Price")       #The funtion gets as parameter the file directly.

            # Add a customer. That by creating a new instance of a Bill class and is append to the list customers.
            elif selected_option == "2":    
                while True:
                    try:
                        customer = input("Please type the new customer's name: ").strip().capitalize()
                        if re.search(r"^[a-zA-Z]{3,12}$|^[a-zA-Z]{3,12} [a-zA-Z]{3,12}$", customer):
                            break
                        else:
                            raise TypeError
                    except TypeError:
                        print("Please ensure to enter only a first name or a first and last name format. No digits or special characters are allowed.")
                        print("Also the accepted range is from 3 to 12 letters each.")
                        pass
                if checking_existing_customer(customer, customers) == (False, False):
                    # Here we are making an instance of a Bill class with a new customer. 
                    customers.append(Bill(customer))   
                    # Here we are controling the index of the list every time a customer is added.
                    customers_index = len(customers) - 1
                    listed_current_menu = open_csv_to_read(menu)
                    listed_modified_menu = add_items_to_customer(customer, listed_current_menu, customers_index)
                    open_csv_to_write(menu, listed_modified_menu, "Item", "Price", "Stock")
                else:
                    print(f"The customer {customer} already exists.")

            # Indicates how many active customers there are and also enumerates them. 
            elif  selected_option == "3":   
                print(f"Now we have {len(customers)} active customer(s):")
                for index, c in enumerate(customers):
                    print(f"Customer {index + 1}.- {c.customer_name}")

            # Check the current bill of a customer.
            elif selected_option == "4":
                customer = input("Please type the name of the customer whose bill you want to check:").strip().capitalize()
                name, index = checking_existing_customer(customer, customers)
                if name:
                    customers[index].tap(19)
                else:
                    print(f"Customer {customer} not found. Ensure you type the correct name, otherwise they don't have an account with us.")
            
            # This option is to add an item to an existing customer's bill.
            elif selected_option == "5":
                customer = input("Which customer would you like to add an item? ").strip().capitalize()
                name, index = checking_existing_customer(customer, customers)
                if name:
                    listed_current_menu = open_csv_to_read(menu)
                    listed_modified_menu = add_items_to_customer(name, listed_current_menu, index)
                    open_csv_to_write(menu, listed_modified_menu, "Item", "Price", "Stock")
                else:
                    print(f"Customer {customer} not found. Ensure you type the correct name, otherwise they don't have an account with us.")

            # Once a customer wants to pay, this option will print the customer invoice as a PDF.
            elif selected_option == "6":
                customer = input("Please type the customer's name who is going to pay their bill: ").strip().capitalize()
                name, index = checking_existing_customer(customer, customers)
                if name:
                    tip_percent = int(input(f"Please enter the percentage {customer}'d like to tip: "))
                    customers[index].invoice(name, tip_percent)
                    print(f"Thanks, {name}, for your purchase, your invoice has been printed as a PDF. Please come back soon! Goodbye")
                    customers[index].delete_customer(customer) 
                    customers.pop(index)
                else:
                    print(f"Customer {customer} not found. Ensure you type the correct name, otherwise they don't have an account with us.")

            # Add new item to the current menu.
            elif selected_option == "7":
                add_items_to_menu(menu)

            # Delete item from the current menu.
            elif selected_option == "8":
                delete_product_to_menu(menu)

            # Show the stock the current stock of the menu.
            elif selected_option == "9":
                listed_current_menu = open_csv_to_read(menu)
                show_table_in_terminal(listed_current_menu, "Item", "Stock")

            # Add stock to the items in the current menu.
            elif selected_option == "10":
                add_stock(menu)

            # Exit the programm.
            elif selected_option == "11":
                raise SystemExit

        except SystemExit:
            print("Thanks for using __BADR__BAR__RESTAURANT__RUNNER__ See you soon!")
            break

def presentation():
    print("Welcome to __BADR__BAR__REATAURANT__RUNNER__")
    for o in options:
       time.sleep(0.01)
       print(f"Option: {options[o]} {o}")

def selection(option_number):
    if re.search(r"^0$|^[1][0-1]?$|^[2-9]$", option_number):
        return option_number
    else:
        raise ValueError

def open_csv_to_read(csv_file):
    try:
        with open(csv_file, "r", newline="") as listed_file:
            reader = list(csv.DictReader(listed_file))
            return reader
    except (FileNotFoundError):
        print("File not found, ensure you have the file.csv you want to read in the same folder as this file.")

def show_table_in_terminal(actual_menu, column_a, column_b):
    try:
        filtered_menu = [{key: i for key, i in a.items() if key in [column_a, column_b]} for a in actual_menu]
        print(tabulate(filtered_menu, headers="keys", tablefmt="grid"))
    except (TypeError, KeyError):
        print("Check if the menu.csv file exist in the same folder as this file and also if it has the correct format.")
        pass

def checking_existing_customer(name, customers_list):
    if len(customers_list) == 0:
        return False, False
    else:
        active_customers = [customer.customer_name for customer in customers_list]
        if name in active_customers:
            return name, active_customers.index(name)
        else:
            return False, False

def add_items_to_customer(customer_name, listed_menu, customer_index):
    global afirm
    global customers
    try:
        current_menu_products = [row["Item"] for row in listed_menu]
    except TypeError:
        return ""
    else:
        is_ordering = "yes"
        while is_ordering in afirm:
            customer_order = input(f"Please {customer_name} tell us your order: ").strip().lower()
            if customer_order in current_menu_products:
                for menu in listed_menu:
                    if menu["Item"] == customer_order:
                        if int(menu["Stock"]) > 0:
                            customers[customer_index].order(customer_order)
                            menu["Stock"] = int(menu["Stock"]) - 1
                        else:
                            print("Sorry, by the moment we don't have stock of that item")
                        break
            else: 
                print("Sorry, we don't have that item in our menu")  
            is_ordering = input(f"{customer_name} do you want another item? ").lower().strip()
        print(f"{customer_name} feel free to ask for another item whenever you want!")
        return listed_menu

def open_csv_to_write(csv_file_name, listed, column_a, column_b, column_c):
    with open(csv_file_name, "w", newline="") as file:
        writing = csv.DictWriter(file, fieldnames=[column_a, column_b, column_c])
        writing.writeheader()
        writing.writerows(listed)

def add_items_to_menu (csv_file):
    new_menu_item = input("Type the name of the new item to put it in the existing menu: ").strip().lower()
    reader = open_csv_to_read(csv_file)
    items_in_menu = [row["Item"] for row in reader]
    if new_menu_item in items_in_menu:
        print(f"{new_menu_item} already exist in the menu")
    else:
        new_item_price = checking_integer("Price")
        new_item_stock = checking_integer("Stock")
        with open(csv_file, "a", newline="") as csv_menu:
            writer = csv.DictWriter(csv_menu, fieldnames=["Item", "Price", "Stock"])
            writer.writerow({"Item": new_menu_item, "Price": f"${new_item_price}", "Stock": new_item_stock})

def delete_product_to_menu (csv_file):
    product_to_delete = input("Type the name of the product you want to delete: ").strip().lower()
    reader = open_csv_to_read(csv_file)
    items_in_menu = [row["Item"] for row in reader]
    if product_to_delete not in items_in_menu:
        print("This product does not exist")
    else:
        current_menu = [row for row in reader if row["Item"] != product_to_delete]
        return open_csv_to_write("./menu.csv", current_menu, "Item", "Price", "Stock")

def add_stock(csv_file):
    product_to_add = input("Type the name of the item you want to add stock: ").strip().lower()
    new_stock_menu = []
    reader = open_csv_to_read(csv_file)
    stock_existing_products = [row["Item"] for row in reader]
    if product_to_add in stock_existing_products:
        amount_to_add = checking_integer("Amount of stock to add")
        for row in reader:
            if row["Item"] == product_to_add:
                new_stock_menu.append({"Item": row["Item"], "Price": row["Price"], "Stock": str(int(row["Stock"])+amount_to_add)})
            else:
                new_stock_menu.append({"Item": row["Item"], "Price": row["Price"], "Stock": row["Stock"]})
        return open_csv_to_write("./menu.csv", new_stock_menu, "Item", "Price", "Stock")
    else:
        print("This product does not exist")

def checking_integer(input_description):
    while True:
        try:
            number_to_check = input(f"{input_description}: ")
            return int(number_to_check)
        except ValueError:
            print("You have to enter a intenger")
            pass

if __name__== "__main__": 
  main()