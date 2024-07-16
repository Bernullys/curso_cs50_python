import time
import csv
from bill import Bill

options = {
    "Show the menu": 1,     # This option will call a function that will open a csv_menu.csv file wich has the current menu.
                            # Show_menu accepts a csv file as argument. In this app is the menu by default.
                            # Then this same function will store the menu in a list and then print it in the terminal. 
                            # (The idea is to put son style in this print)
    "Initialize a bill": 2, # Every time a customer is been initialized, the app will keep track with a respald of its bill in a csv file.
                            # So in a csv file named current_bills.csv will be write the name of each customer, the item, its price and the entire
                            # date when was make the item.
    "Check active customers": 3,    # This option prints the lenght of the list of custumers and then sweep the list to show each customer
                                    # with its index.
    "Check the bill by customer": 4,# This option ask for the customer name and then it shows the bill of that customer in the Terminal.
    "Add item to an active customer": 5,    # This option is to add an item to an existin customer's bill. 
    "Confirm paiment and save bill in a pdf": 6,    # Once a costumer wants to pay, this option will print a the 
                                                    # customer invoice as a pdf.
                                                    # Now the costumer and its orders must be take out
                                                    # of the custumers list, and their items out of current_bills.csv. 
    "Add a new product to the menu": 7,             # Ready - Add description to this function.
    "Delete a product from the menu": 8,            # Ready -Add description to this function.
    "Show stock": 9,                                # menu.csv file has a third column which specified the amount of stock each product has.
                                                    # With this function I can show the stock of each product.
    "Add stock to a specific product": 10,
    "Quit": 11,
    # Would be cool if I can check the amount in bitcoins currency
}

def main():
    
    customers = []  # In this list we will store all the coustumers bill instancies.
    n = 0           # n is to initialized the index of costumer in the list costumers. 
                    # So each time a costumer is added don't overlap the previews one.
    presentation()  # Presentation function is used to run the program. Presentention prints all the options the program has.

    #this while loop keep the program runing.
    while True:
        selected_option = selection()   #selection function take and return the number of the selected option.
        
        if selected_option == "1":      #show_menu function prints the menu. So the user can indicate which item wants.
            show_menu("menu.csv")       #The funtion gets as parameter the file directly.

        elif selected_option == "2":    # add a custumer. That by creating a new instance of a Bill class and is append to the list custumers.
            n += 1                      # Here we are controling the index of the list every time a customer is added.
            customer_name = input("Please type the customer name: ")
            customers.append(Bill(customer_name))   # Here we are making an instance of a Bill class with a new customer. 
            is_ordering = "yes"                     # we assume when a  customer is initialized, will ask for at least an item.
            while is_ordering == "yes":
                customers[n-1].order(input(f"Please {customer_name} tell us your order: ")) # order method is appending items to each customer instance.
                is_ordering = input(f"{customer_name} do you want another item? ")          # Also order method is writing the order with all details in a csv file.

        elif  selected_option == "3":   
            print(f"Now we have {len(customers)} active(s):")
            for index, c in enumerate(customers):   # To achive this I'm usinng enumerate build in function. (Whatch for documentation)
                print(f"Customer {index + 1}.- {c.customer_name}")

        elif selected_option == "4":    # This option is checking for the exact name of the costumer and then check in the Bills class the instance-
                                        # which match that name. That method by default prints the bill in the terminal.
                                        # Then we are passing a 19% of taxes directly to the total amount.
            check_customer = input("Please type the customer name: ")
            for c in customers:
                if c.customer_name == check_customer:
                    c.tap(19)
        
        elif selected_option == "5":    # First of all we check if the costumer exist.
                                        # Then we check for the index and the name of the costumer, so then we can add an order to the index
                                        # of that intance of the costumers list
            check_existing_customer = input("Which customer do you want to add an item? ")
            for index, c in enumerate(customers): 
                if c.customer_name == check_existing_customer:
                    is_ordering_again = "yes"
                    while is_ordering_again == "yes":   # (Use a list with all the options to be a yes answerd).
                        customers[index].order(input(f"{c.customer_name} please tell us your new order: "))
                        is_ordering_again = input(f"{c.customer_name} do you want another item? ")

        elif selected_option == "6":
            check_customer = input("Please type the customer which is going to pay its bill: ")
            for c in customers:
                if c.customer_name == check_customer:   # Here we match the customer's name with its bill.
                    tip_percent = int(input(f"{check_customer} how much will be your tip? "))
                    c.invoice(check_customer, tip_percent)           # invoice method is creating a pdf with the customer's invoice.
                    print(f"Thank's {c.customer_name} for your purchase, your invoice has been printed as a pdf. Please come back soon! Bye")
                    # Now this next method delete this customer from the csv file which has all the items.
                    c.delete_customer(check_customer)

        elif selected_option == "7":
            add_items_to_menu("./menu.csv")

        elif selected_option == "8":
            delete_product_to_menu("./menu.csv")

        elif selected_option == "9":
            show_stock("menu.csv")

        elif selected_option == "10":
            add_stock("menu.csv")

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

def add_items_to_menu (csv_file):
    # I have to check first if the item I want to add does not exist
    new_menu_item = input("Type the name of the new item to put it in the existing menu: ")
    
    items_in_menu = []
    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items_in_menu.append(row["item"])

        if new_menu_item in items_in_menu:
            print("This item already exist in the menu")
        else:
            new_menu_price = input("Price of the new item in the menu: ")
            new_item_stock = input("Stock of this new product: ")
            with open(csv_file, "a", newline="") as csv_menu:
                writer = csv.DictWriter(csv_menu, fieldnames=["item", "price", "stock"])
                writer.writerow({"item": new_menu_item, "price": new_menu_price, "stock": new_item_stock})

def delete_product_to_menu (csv_file):
    # I have to check if the product I want to delete does exist.
    product_to_delete = input("Type the name of the product you want to delete: ")
    items_in_menu = []
    all_menu = []
    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items_in_menu.append(row["item"])
            all_menu.append(row)
        print(items_in_menu)
        if product_to_delete not in items_in_menu:
            print("This product do not exist")
        else:
            for i in items_in_menu:
                print(i)
            current_menu = [row for row in all_menu if row["item"] != product_to_delete]
            print(current_menu)
            with open(csv_file, "w", newline="") as file:
                update_menu = csv.DictWriter(file, fieldnames=["item", "price"])
                update_menu.writeheader()
                update_menu.writerows(current_menu)  

def show_stock(csv_file):                                   # Here we get the menu as parameter.                                              
                                                            # We read the file and then append it to a list.
   with open (csv_file) as csv_menu:                        # Finally we print the items and price in the terminal.
    reader = list(csv.DictReader(csv_menu))
    for row in reader:
       print(f"{row['item']}  {row['stock']}")

def add_stock(csv_file):
    product_to_add = input("Type the name of the item you want to add stock: ")
    amount_to_add = input(f"Type the amount of {product_to_add} you want to add ")
    new_stock_menu = []
    with open(csv_file) as csv_menu:
        reader = list(csv.DictReader(csv_menu))
        for row in reader:
            if row["item"] == product_to_add:
                row["stock"] = int(row["stock"]) + int(amount_to_add)
            new_stock_menu.append({"item": row["item"], "price": row["price"], "stock": str(row["stock"])})

    with open(csv_file, "w", newline="") as csv_menu:
        writer = csv.DictWriter(csv_menu, fieldnames=["item", "price", "stock"])
        writer.writeheader()
        writer.writerows(new_stock_menu)
                

# I'm going to create a function to open a csv file to read and then returns a variable to be manipulated.

def open_csv_to_read (csv_file):
    ...


if __name__== "__main__": 
  main()