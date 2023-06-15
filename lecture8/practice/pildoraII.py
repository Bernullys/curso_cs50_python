class Coche():
    def __init__(self):                 #Constructor
        self.largo_chasis = 250              #Estado inicial
        self.ancho_chasis = 120
        self.ruedas = 4
        self.enmarcha = False

    #comportamiento o metodo:
    def encender(self, arrancar):
        self.arrancar = arrancar
        if self.arrancar:
            return "El coche esta encendido"
        else:
            return "El coche esta apagado"

    def estado(self):
        print(f"El coche tiene {self.largo_chasis} de largo, {self.ancho_chasis} de ancho, {self.ruedas} ruedas")


coche1 = Coche()
print(coche1.encender(True))
coche1.estado()

coche2 = Coche()
print(coche2.encender(False))
coche2.estado()