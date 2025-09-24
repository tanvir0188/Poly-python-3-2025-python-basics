class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)


class Triangle:
    def __init__(self, a, b, c, height=None):
        self.a = a
        self.b = b
        self.c = c
        self.height = height
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        if self.height:
            return 0.5 * self.b * self.height
        else:
            s = self.perimeter() / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side


rect = Rectangle(2, 4)
tri = Triangle(3, 4, 5)
sq = Square(5)

print("Rectangle: Area =", rect.area(), ", Perimeter =", rect.perimeter())
print("Triangle: Area =", tri.area(), ", Perimeter =", tri.perimeter())
print("Square: Area =", sq.area(), ", Perimeter =", sq.perimeter())
