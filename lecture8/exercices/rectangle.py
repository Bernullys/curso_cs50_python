class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f" Un rectangulo es una figura geometrica bidimensional de cuatro lados de iguales dimensiones por pares"

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
    
    @classmethod
    def dimensions(cls):
        width = int(input("Width = "))
        height = int(input("Height = "))
        return cls(width, height)

def main():
    dimensions = Rectangle.dimensions()
    print(dimensions)
    print(Rectangle.area(dimensions))
    print(dimensions.area())


if __name__=="__main__":
    main()