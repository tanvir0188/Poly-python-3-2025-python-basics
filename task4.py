'''Task 1:
Create a Family object. It should have attribute such as my_name, father_name, mother_name, sister_name, brother_name
You have to create the class using a constructor. Initiate it and set values to the attributes.'''


class Family:

    def __init__(self, fathername, mothername, brothername, sistername, familymember, myname):
        self.father_name = fathername
        self.mother_name = mothername
        self.brother_name = brothername
        self.sister_name = sistername
        self.family_member = familymember
        self.my_name = myname

family= Family('Aksh', 'Ava', 'Rana', 'Rimi', 5, 'Suva')
print(f'father name: {family.father_name},mother name: {family.mother_name}, brother name: {family.brother_name}, sister name: {family.sister_name}, family member: {family.family_member}, my name: {family.my_name}')

'''Task 2:
Create a rectangle, a triangle and a square object.
Initialize them. Find out the area and perimeter of each object.

for example,

a rectangle has length and width. it so the rectangle object should take  Rectangle(2, 4)
the area should be area = 2*4. But you must do this by accessing the attributes of the created object. Similarly Do all of them.

NB: If you can use class method then do it. Otherwise you can use constructor only'''

# for Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length  
        self.width = width     
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(4,7)
print(f'rectangle length: {rectangle.length},rectangle width: {rectangle.width},rectangle area: {rectangle.area()}, rectangle perimeter: {rectangle.perimeter()}')

#for square

class Square:
    def __init__(self, side):
        self.side = side   
    
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side

square = Square(4)
print(f'side={square.side}, square area={square.area()}, square perimeter={square.perimeter()}')

# for triangle
import math

class Triangle:
    def __init__(self, a, b, c, base=None, height=None):
        self.a = a      
        self.b = b     
        self.c = c      
        self.base = base
        self.height = height
    
    def area(self):
        if self.base and self.height:   
            return 0.5 * self.base * self.height
        else:   
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c



triangle = Triangle(2,4,6,base=2, height=4 )
print(f"Triangle: sides={triangle.a},{triangle.b},{triangle.c}, area={triangle.area()}, perimeter={triangle.perimeter()}")

# if triangle is right-angled

class RightTriangle:
    def __init__(self, base, height,):
        self.base = base
        self.height = height
        self.hypotenuse = (base**2 + height**2) ** 0.5
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse



righttriangle = RightTriangle(6, 12)

print(f"Right-angled Triangle: base={righttriangle.base}, height={righttriangle.height}, hypotenuse={righttriangle.hypotenuse:.2f}, area={righttriangle.area()}, perimeter={righttriangle.perimeter():.2f}")
