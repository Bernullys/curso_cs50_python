# I will make a class name Bike

class Bike:
    #This are the properties that has my bike:
    wheels = 2
    color = "gray"
    type = "montainbike"
    kg_weith = 12
    psi = 20

    #this is a method of the class Bike:
    def inflate_to_n_psi(self, psi):
        self.psi = psi
        return f"Wheels are now at {psi} psi"



ber = Bike()
print(ber.color)
print(ber.kg_weith)
print(ber.psi)
ber_wheels_pressure = ber.inflate_to_n_psi(40)
print(ber_wheels_pressure)
print(ber.psi)
