class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.model = "Camry"
        self.year = 2019
        self.color = "redwine"
        self.on = True
    
    def turn_on(self):
        #self.on = on
        if self.on:
            return "Is on alrady"
        else:
            self.on = True
            return "Now is on"

movil = Car()
print(movil.brand)
print(movil.on)
print(movil.turn_on())