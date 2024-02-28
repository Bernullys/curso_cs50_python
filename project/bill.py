import csv

menu = {}
with open ("./menu.csv") as csv_menu:
    reader = csv.DictReader(csv_menu)
    for row in reader:
        menu[row["item"]] = float(row["price"])

#using this dictionary I can have acces to the price of any item by name



print(menu)
 

class Bill:
    def __init__(self, custumer_name):
        self.custumer_name = custumer_name
        self.items = []
        self.amount = 0
    
    def order(self, items):
        self.items.append(items)
        self.amount += menu[items]

    def tap(self, taxes, tips):
        tax = self.amount*taxes/100
        tip = self.amount*tips/100
        total = self.amount + tax + tip
        for item in self.items:
            print(f"{item}  {self.amount}")
        print(tax)
        print(tip)
        print(total)


def show_menu(csv_file):
   menu = []
   with open (csv_file) as csv_menu:
    reader = csv.reader(csv_menu)
    for row in reader:
        menu.append({"item": row[0], "price": row[1]})
    for m in menu:
       print(f"{m['item']}  {m['price']}")