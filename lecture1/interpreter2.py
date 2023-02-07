def main ():
    arg = input("Expression: ")
    interpreter(arg)

def interpreter(eq):
    x, y, z = eq.split(" ")
    x = int(x)
    z = int(z)                                      # Como hago para retornar los resultados en vez de imprimirlos desde la funcion ?

    if y == "+":
        suma = float(x+z)
        return suma
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/" and z != 0:
        print(round(float(x/z),1))
    elif z == 0: print("No se puede dividir entre cero")

main()
