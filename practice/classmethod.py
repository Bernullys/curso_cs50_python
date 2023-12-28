class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def claculate_area(self):
        return self.width*self.height

    @classmethod
    def new_square(cls, side_lenght):
        return cls(side_lenght, side_lenght)


rect = Rectangle.new_square(2)
print(rect.claculate_area())


################################################

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

# ingredients = ["cheese", "onions", "spam", "pineapple"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)


####################################################

class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    @staticmethod
    def area(w, h):
        return w * h

w = 5
h = 4

print(Shape.area(w, h))