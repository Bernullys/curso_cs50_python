class Car():
    def __init__(self, model, color, brand, turnon):
        self.model = model
        self.color = color
        self.brand = brand
        self.turnon = turnon
    
    def start(self):
        if self.turnon:
            return "is on"
        else:
            return "is off"
    
    def my_car(self):
        return f"My car is a {self.brand} {self.model} color {self.color}"

bercar = Car("Grandi10", "silver", "Hyundai", False)
print(bercar.model)
bercar.model  = "Toyota"
print(bercar.model)
print(bercar.start())
print(bercar.my_car())