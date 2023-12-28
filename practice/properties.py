class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)

#pizza.pineapple_allowed = True      #This will show an error because can't set attribute

###########################################

class Person:
    def __init__(self, age):
        self.age = age
    
    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False

####################################################
