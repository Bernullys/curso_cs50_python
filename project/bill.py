import csv

menu = {
    "hamburger": 30,
    "coke": 10,
    "fries": 15
}
 
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


