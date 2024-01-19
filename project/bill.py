menu = {
    "hamburger": 30,
    "coke": 10,
    "fries": 15
}

class Bill:
    def __init__(self):
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



