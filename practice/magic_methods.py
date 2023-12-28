# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)

# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first + second
# print(result.x)
# print(result.y)


# ###################################################

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
    
#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         return "\n".join([self.cont, line, other.cont])

# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)


# ####################################################

# class SpecialString2:
#     def __init__(self, cont):
#         self.cont = cont

#     def __gt__(self, other):
#         for index in range(len(other.cont)+1):
#             result = other.cont[:index] + ">" + self.cont
#             result += ">" + other.cont[index:]
#             print(result)

# spam = SpecialString2("spam")
# eggs = SpecialString2("eggs")
# spam > eggs

# ########################################################

# import random

# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont

#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]
    
#     def __len__(self):
#         return random.randint(0, len(self.cont)*2)

# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])


##############################################

class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

    def __add__(self, other):
        return Shape(self.w + other.w, self.h + other.h)

    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input("Widht1: "))
h1 = int(input("Height1: "))
w2 = int(input("Widht2: "))
h2 = int(input("Height2: "))

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)

result = s1 + s2

print(result.area())
print( s1 > s2)