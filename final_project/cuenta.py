class Cuenta:
    def __init__(self, acumulado):
        self.acumolado = acumulado


    def pedidos(self):
        ...


products = {

    "Burger": "$5",
    "Pizza": "$8",
    "Fries": "$3",
    "Drink": "$2",
}

Bernardo = Cuenta(0)

for key, value in products.items():
    setattr(Bernardo, key, value)

print(Bernardo.Burger)