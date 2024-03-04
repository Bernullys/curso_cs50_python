import csv

#This is were I'm taking the menu to be used in the Bill class.
#bringing this dictionary I can have access to the price of any item by name.
menu = {}
with open ("./menu.csv") as csv_menu:
    reader = csv.DictReader(csv_menu)
    for row in reader:
        menu[row["item"]] = float(row["price"])
 

#With this class I'm creating costumers  by name and adding the items to their order list.
class Bill:
    def __init__(self, custumer_name):
        self.custumer_name = custumer_name
        self.items = []
        self.amount = 0
    
    def order(self, items):
        self.items.append(items)
        self.amount += menu[items]

    def tap(self, taxes):
        tax = self.amount*taxes/100
        tip = self.amount*int(input("Persent of tip: "))/100
        total = self.amount + tax + tip
        for item in self.items:
            print(f"{item}  {menu[item]}")
        print(tax)
        print(tip)
        print(total)