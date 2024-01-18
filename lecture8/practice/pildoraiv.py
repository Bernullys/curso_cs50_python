class Car():
    def __init__(self, model, color, brand, turnon):
        self.__model = model
        self.__color = color
        self.__brand = brand
        self.__turnon = turnon
    
    def start(self):
        if self.__turnon:
            return "is on"
        else:
            return "is off"
    
    def my_car(self):
        return f"My car is a {self.__brand} {self.__model} color {self.__color}"

bercar = Car("Grandi10", "silver", "Hyundai", False)
#print(bercar.model)
bercar.__model  = "Toyota" # Esto no se debe hacer porque por convension, el underscore indica que no modifiquemos esa parametro.
print(bercar.__model)
print(bercar.start())
print(bercar.my_car())