from xml.sax.handler import feature_validation


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))

#######################################

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(19))
print(is_even(24))

######################################

def convert(num):
    if num == 0:
        return 0
    return (num % 2 + 10 * convert(num // 2))

print(convert(8))


#######################################

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))


#########################################3

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print (power(2, 3))


################
a = (lambda x: x **2) (7)

print(a)