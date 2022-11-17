def main():

    exp = get_operation(input("Expression: "))


def get_operation(entrada):

    expression = str(entrada)

    x, y, z = expression.split(" ")
    a = int(x)
    b = int(z)

    if y == "+":
        print(float(a+b))
    elif y == "-":
        print(float(a-b))
    elif y == "*":
        print(float(a*b))
    elif y == "/":
        print(float(a/b))

main()


