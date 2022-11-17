def main():

    mass = int(input("m: "))
    c = 300000000

    E = energy(mass, c)

    print("E: ", E)


def energy(mass, c):
    
    E = mass * pow(c, 2)
    return E

main()