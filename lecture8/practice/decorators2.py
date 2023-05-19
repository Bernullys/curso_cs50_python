def decorator_function(parameter_function):

    def in_function(*args, **kwargs):             # *args especifica que la funcion puede recibir n parametros

        print("Se va a realizar una operación")

        parameter_function(*args, **kwargs)

        print("Se realizo una operación")

    return in_function


@decorator_function
def sum(a, b):
    return (a+b)

@decorator_function
def res(a, b):
    print(a-b)

@decorator_function
def power(base, exp):
    return pow(base, exp)


print(sum(10, 40))

res(8, 4)

print(power(base=2, exp=4))