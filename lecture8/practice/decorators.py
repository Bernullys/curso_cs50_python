def decorator_function(parameter_function): # el argumento es la funcion que decoramos
    def in_function():

        # acciones que "decoran"
        print("Se va a realizar un calculo")

        # acciones que ejecutan las funciones iniciales
        parameter_function()

        #mas acciones que "decoran"
        print("Se realizo un calculo")

    return in_function


@decorator_function
def sum():
    print(10 + 10)

def res():
    print(10 - 10)

sum()
res()