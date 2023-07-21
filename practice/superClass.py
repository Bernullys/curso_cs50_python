class Animal:     # Superclass
    def __init__ (self, name, color):
        self.name = name
        self.color = color
    
class Cat(Animal):  # Inherit class
    def purr(self):
        print("Purrr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

######################################################

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):     # Inherit with same attribute -- overrides the superclass attribute
        print("Woof!")

husky = Dog("Max", "grey")
husky.bark()

########################################################

#super() is a function in classes

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()


#####################################################

class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        print(self.w * self.h)

class Rectangle(Shape):
    def perimeter(self):
        print(2 * (self.w + self.h))

w = int(input("Widht: "))
h = int(input("Height: "))

r = Rectangle(w, h)
r.area()
r.perimeter()