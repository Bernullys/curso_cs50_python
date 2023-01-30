# this function uses two arguments. But actually if I use c as an constant, I could use only one.
# Also here I use the function pow to elevate a int to a power of that number.

def main():

    mass = int(input("m: "))
    E = energy(mass)
    print("Energy in jouls is ", E)

def energy(mass):

    c = 300000000
    E = mass*pow(c,2)
    return E

main()