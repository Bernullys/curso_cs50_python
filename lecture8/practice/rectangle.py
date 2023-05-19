from curses.textpad import rectangle


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return f" Area = {self.height * self.width} m^2"
    
    def perimeter(self):
        return f"Perimeter = {(self.height + self.width) * 2} m"

    def draw_area(self):
        rectangle_area = ""
        for w in range (self.width):
            rectangle_area += "#"*self.height + "\n"
        return rectangle_area

    def draw_perimeter(self):
        rectangle_perimeter = ""
        rectangle_perimeter += "*" * self.width + "\n"

        for h in range(self.height-2):
            rectangle_perimeter += "*" + " " * (self.width -2) + "*" + "\n"
        
        rectangle_perimeter += "*" * self.width
        return rectangle_perimeter



court = Rectangle(20, 50)

print(court.area())
print(court.perimeter())
print(court.draw_area())
print(court.draw_perimeter())
