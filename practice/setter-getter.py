class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "casa":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)

pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


###########################################################

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -=1

    @property
    def isAlive(self):
        return self._lives

p = Player("Bernardo", 5)

i = 1

while True:
    p.hit()
    print("Hit # "+ str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break