#Create a Family object. It should have attribute such as my_name, father_name, mother_name, sister_name, brother_name
#You have to create the class using a constructor. Initiate it and set values to the attributes.


class Family:
    def __int__ (self, fathername, mothername, sistername, brothernam, myname):
        self.father_name=fathername
        self.mother_name=mothername
        self.sister_name=sistername
        self.brother_name=brothername
        self.my_name=myname
 family=Family('matin','ripa','maisha', 'raiyan','shifa')
print(f'father name: {Family.father_name}, mother name: {Family.mother_name}, sister name: {Family.sister_name}, brother name: {Family.brother_name}, my name: {Family.my_name}')



#Create a rectangle, a triangle and a square object.
#Initialize them. Find out the area and perimeter of each object.

#for example,

#a rectangle has length and width. it so the rectangle object should take  Rectangle(2, 4)
#the area should be area = 2*4. But you must do this by accessing the attributes of the created object. Similarly Do all of them.

#NB: If you can use class method then do it. Otherwise you can use constructor only


import math
class Rectangle:
     def __int__ (self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)

rectangle=Rectangle(4,5)
print(f'rectangle length {rectangle.length}, rectangle width {rectangle.width}, rectangle area {rectangle.area()}, rectangle perimeter {rectangle.perimeter()}')
