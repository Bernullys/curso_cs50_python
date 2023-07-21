def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

def primeGenerator(a, b):
    for i in range(a, b):
        if isPrime(i):
            yield i

a = int(input("from: "))
b = int(input("to: "))

print(list(primeGenerator(a, b)))