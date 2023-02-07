eq = input("Expression: ")

x, y, z = eq.split(" ")

x = int(x)
z = int(z)



if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/" and z != 0:
    print(float(x / z))
    else: print("No se puede dividir entre cero")

