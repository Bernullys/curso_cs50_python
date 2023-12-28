from sys import float_repr_style


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("Beige", 4)
rover = Cat("Brown", 4)
stumpy = Cat("Yellow", 3)


print(felix.color) # attribute color
print(felix.legs) # attribute legs
print(felix) # memory space

#print(felix.legs(2)) #can't do this.
felix = Cat("blue", 5)
print(felix.color)


#############################################

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "Brown")
print(fido.name)
fido.bark()


#################################################

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(f"{self.name} (Level {self.level})")


get_name = input("Name: ")
get_level = input("Level: ")

player_n = Player(get_name, get_level)

player_n.intro()