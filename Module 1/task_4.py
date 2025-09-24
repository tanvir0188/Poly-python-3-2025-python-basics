#Task 1:
#Create a Family object. It should have attribute such as my_name, father_name, mother_name, sister_name, brother_name
#You have to create the class using a constructor. Initiate it and set values to the attributes.


class Family:

  def __int__(self, my_name, father_name, mother_name, sister_name, brother_name):
      self.my_name=my_name
      self.father_name=father_name
      self.mother_name=mother_name
      self.sister_name=sister_name
      self.brother_name=brother_name

family = Family('Maria', 'Borhan', 'Maya', 'Rabeya', 'Mohin')
print(f'family_name:{my.my_name}, father_name:{father.father_name}, family_name:{mother.mother_name}, family_name:{sister.sister_name}, family_name:{brother.brother_name}')



#Task 2:
#Create a rectangle, a triangle and a square object.
#Initialize them. Find out the area and perimeter of each object.

#for example,

#a rectangle has length and width. it so the rectangle object should take  Rectangle(2, 4)
#the area should be area = 2*4. But you must do this by accessing the attributes of the created object. Similarly Do all of them.

#NB: If you can use class method then do it. Otherwise you can use constructor only

class Rectangle:
   def __init__(self, width, height):
      self.width= width
      self.height= height
       
   def area(self):
        return self.width*self.height
   def perimeter(self):
        return 2*(self.width+self.height)
rectangle= Rectangle(2,3)
print(f'rectangle width: {rectangle.width}, rectangle height: {rectangle.height}, rectangle area: {rectangle.area()}, rectangle perimeter: {rectangle.perimeter()}')
      
class Square:
    def __init__(self, side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
square= Square(4)
print(f'square side: {square.side}, square area: {square.area()}, square perimeter: {square.perimeter()}')

class Triangle:
    def __init__(self, base, height, hypotenuse):
        self.base= base
        self.height= height
        self.hypotenuse= hypotenuse
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.base+self.height+self.hypotenuse
triangle= Triangle(2,3,4)
print(f'Triangle area: {triangle.area}, Triangle perimeter: {triangle.perimeter}')
