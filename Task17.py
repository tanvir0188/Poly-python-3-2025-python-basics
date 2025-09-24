"""
Create a rectangle, a triangle and a square object.
Initialize them. Find out the area and perimeter of each object.

for example,

a rectangle has length and width. it so the rectangle object should take  Rectangle(2, 4)
the area should be area = 2*4. But you must do this by accessing the attributes of the
created object. Similarly Do all of them.

NB: If you can use class method then do it. Otherwise you can use constructor only
"""


# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Triangle class
class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Square class
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Create Objects 
rect = Rectangle(2, 4)
tri = Triangle(base=3, height=4, side1=3, side2=4, side3=5)
sq = Square(5)


print("Rectangle:")
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

print("\nTriangle:")
print("Area:", tri.area())
print("Perimeter:", tri.perimeter())

print("\nSquare:")
print("Area:", sq.area())
print("Perimeter:", sq.perimeter())
