class Coche():
    #propiedades:
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    enmarcha = False

    #comportamiento o metodo:
    def encender(self):
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:
            return "Coche encendido"
        else:
            return "Coche apagado"


miCoche = Coche() # instanciar una clase
print(miCoche.largo_chasis)
miCoche.encender()
print(miCoche.enmarcha)
print(miCoche.estado())
