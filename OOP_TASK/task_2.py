import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        hypo = math.sqrt(self.base**2 + self.height**2)
        return self.base + self.height + hypo


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

  
rectangle = Rectangle(4, 5)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("--------------------")

triangle = Triangle(3, 4)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

print("--------------------")

square = Square(4)
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())
