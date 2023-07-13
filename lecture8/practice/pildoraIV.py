class Coche():
    def __init__(self, largo_chasis, ancho_chasis, ruedas, enmarcha):   #Constructor
        self.__largo_chasis = largo_chasis                              #Estado inicial NO Modificable desde afuera de la clase
        self.__ancho_chasis = ancho_chasis
        self.__ruedas = ruedas
        self.__enmarcha = enmarcha

    #comportamiento o metodo:
    def encender(self, arrancar):
        self.arrancar = arrancar
        if self.arrancar:
            return "El coche esta encendido"
        else:
            return "El coche esta apagado"

    def estado(self):
        print(f"El coche tiene {self.__largo_chasis} de largo, {self.__ancho_chasis} de ancho, {self.__ruedas} ruedas")


coche1 = Coche(10, 5, 4, True)
coche1.ruedas = 9
coche1.__ruedas = 10
print(coche1.encender(True))
coche1.estado()


