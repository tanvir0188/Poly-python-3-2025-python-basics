#Task-1:
class family:
    member = 'six'
    def __init__(self,father_name,mother_name,sister_name,brother_name,my_name):
        self.father_name= father_name
        self.mother_name= mother_name
        self.sister_name= sister_name
        self.brother_name= brother_name
        self.my_name= my_name
member1= family("asd","bnds","ksjd","djds","jjd")
print(f"family_member:{member1.father_name},{member1.mother_name},{member1.sister_name},{member1.brother_name},{member1.my_name}")

#Task-4:
import math
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        hypo = math.sqrt(self.base**2 + self.height**2)
        return self.base + self.height + hypo

class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side

rectangle = Rectangle(2,4)
print("Rectangle Area:",rectangle.area())
print("Rectangle Perimeter:",rectangle.perimeter())

triangle = Triangle(5,6)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

square = Square(4)
print("Square Area:",square.area())
print("Square Perimeter:",triangle.perimeter())