#Task 1:
class family:
    def __init__ (self,my_name,father_name,mother_name,sister_name):
        self.my_name = my_name 
        self.father_name = father_name
        self.mother_name = mother_name 
        self.sister_name = sister_name

Family1 = family ("Ayesha","Razzak","Kolpona","Marjana")

print (f"{Family1.my_name},{Family1.father_name},{Family1.mother_name},{Family1.sister_name}")


# Task 2 :

class Rectangle:
    def __init__ (self, length , width):
        self.length = length
        self.width = width
    def area (self):
        return (self.length * self.width) 
    def perimeter(self):
        return 2 * (self.length + self.width)   
r = Rectangle (2,4)
print ("Rectangle Area:",r.area() , "Rectangle perimeter:" ,r.perimeter())


class Triangle :
    def __init__(self, base, height, side1, side2, side3):
        self.base = base 
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area (self):
        return (self.base * self.height)
    def perimeter(self):
        return (self.side1 + self.side2 + self. side3)

t = Triangle (4,6,4,6,5)
print (f"Triangle Area:", t.area() ,"Triangle Area:" , t.perimeter() )


class Square :
    def __init__ (self,side):
        self.side = side
    
    def area(self):
        return (self.side * self.side)
    def perimeter (self):
        return (4 * self.side)
s = Square (7)
print (f"Square Area:", s.area() , "Square perimeter:" , s. perimeter() )

