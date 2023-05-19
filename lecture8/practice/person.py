class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello my name is {self.name}, I'm from Venezuela and I'm {self.age} years old"


jefe = Person("Bernardo", 35)

print(jefe.name, jefe.age)

print(jefe.introduce())
