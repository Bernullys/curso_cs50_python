class Coche():
    def __init__(self, largo_chasis, ancho_chasis, ruedas, enmarcha): 
        self.__largo_chasis = largo_chasis                               
        self.__ancho_chasis = ancho_chasis
        self.__ruedas = ruedas
        self.__enmarcha = enmarcha


    def encender(self, arrancar):
        self.arrancar = arrancar

        if self.encender:
            chequeo = self.chequeo_interno()

        if self.arrancar and chequeo:
            return "El coche esta encendido"

        elif self.arrancar and chequeo == False:
            return "No se chequeo bien ---  algo anda mal"

        else:
            return "El coche esta apagado"

    def estado(self):
        print(f"El coche tiene {self.__largo_chasis} de largo, {self.__ancho_chasis} de ancho, {self.__ruedas} ruedas")


    def chequeo_interno(self):      # No tiene sentido acceder a este metodo desde fuera de la clase pero como no esta encapsulado si se puede.
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "not"
        self.puertas = "cerradas"
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False



coche1 = Coche(10, 5, 4, True)
coche1.ruedas = 9
print(coche1.encender(True))
coche1.estado()


