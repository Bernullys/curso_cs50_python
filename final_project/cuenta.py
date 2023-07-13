products = {
    "Burger": 5,
    "Pizza": 8,
    "Fries": 3,
    "Drink": 2,
}

class Tap:

    def __init__(self):
        self.deb = 0
        self.orders = []

    def consumption(self, order):
        self.orders.append(order)
        self.deb += products[order]

    def bill(self, tax, tip):
        self.tax = tax
        self.tip = tip
        taxes = self.deb*self.tax/100
        tips = self.deb*self.tip/100
        total = self.deb + taxes + tips
        print (total)

        for item in self.orders:
            print(f"{item} ------ {products[item]}")

Bernardo = Tap()
Bernardo.consumption("Burger")
Bernardo.consumption("Pizza")
Bernardo.bill(10, 10)
