class Coche():
    def __init__(self, largo_chasis, ancho_chasis, ruedas, enmarcha):   #Constructor
        self.largo_chasis = largo_chasis                                #Estado inicial Modificable desde afuera de la clase
        self.ancho_chasis = ancho_chasis
        self.ruedas = ruedas
        self.enmarcha = enmarcha

    #comportamiento o metodo:
    def encender(self, arrancar):
        self.arrancar = arrancar
        if self.arrancar:
            return "El coche esta encendido"
        else:
            return "El coche esta apagado"

    def estado(self):
        print(f"El coche tiene {self.largo_chasis} de largo, {self.ancho_chasis} de ancho, {self.ruedas} ruedas")


coche1 = Coche(10, 5, 4, True)
coche1.ruedas = 9
print(coche1.encender(True))
coche1.estado()
coche1.largo_chasis = 500
print(coche1.largo_chasis)


