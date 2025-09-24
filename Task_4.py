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
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(2,4)
print("Rectangle Area:",rectangle.area())
print("Rectangle Perimeter:",rectangle.perimeter())
