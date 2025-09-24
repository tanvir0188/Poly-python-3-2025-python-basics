# some animal:practice 
class Dog():
    species="canis familiaris"               #class attribute
    def __init__(self,name,age,color):
        self.dog_name=name
        self.dog_age=age
        self.dog_color=color
        
dog1=Dog("tomy",5,"black")
dog2=Dog("tom",5,"red")
print(f'I have a {dog1.species} dog.my dog name {dog1.dog_name} . this is  {dog1.dog_age} years old.this dog {dog1.dog_color} color is very nice.')

print(f'I have a {dog2.species} dog.my dog name {dog2.dog_name} . this is  {dog2.dog_age} years old.this dog {dog2.dog_color} color is very nice.')

class Cat():
    spacies="Falis cats"
    def __init__(self,name,age,color):
        self.cat_name=name
        self.cat_age=age
        self.cat_color=color
cat1=Cat("jany",1,"white")

print(f"I have a {cat1.spacies} cat .my cat namse is : {cat1.cat_name} . ihis is {cat1.cat_age} yeras old.there {cat1.cat_color} color is very buitifull.")




#Task 1:
#Create a Family object. It should have attribute such as my_name, father_name, mother_name, sister_name, brother_name
#You have to create the class using a constructor. Initiate it and set values to the attribu 

class Family():
    def __init__(self,my_name,father_name,mother_name,brother_name,sister_name):
        self.my_name=my_name
        self.father_name=father_name
        self.mother_name=mother_name
        self.brother_name=brother_name
        self.sister_name=sister_name
        
f1=Family("Yousuf miah","Tukku miah","Rehena begum","Ibrahim miah","asma akter")
print(f"my name is : {f1.my_name} . my father name is : {f1.father_name} . my mother name is : {f1.mother_name} .my brother name is  : {f1.brother_name} . my sister name is {f1.sister_name} ." )

#Task 2:
#Create a rectangle, a triangle and a square object.
#Initialize them. Find out the area and perimeter of each object.

#for example,

#a rectangle has length and width. it so the rectangle object should take  Rectangle(2, 4)
#the area should be area = 2*4. But you must do this by accessing the attributes of the created object. Similarly Do all of them.

#NB: If you can use class method then do it. Otherwise you can use constructor #only

class Square():
    def __init__ (self,base):
        self.base=base
    def area(self):
        return self.base**2
    
 
class Rectangle():
    def __init__ (self,width,hight):
        self.width=width
        self.hight=hight
    def area(self):
        return  self.width * self.hight
    

class Triangle():
    def __init__ (self,base,hight):
        self.base=base
        self.hight=hight
    def area(self):
         return  0.5 * self.base * self.hight
     
square=Square(7)
rectangle=Rectangle(5,7)
triangle=Triangle(5,7)

print ("this squqre area is : ",square.area())
print ("this rectangle area is : ",rectangle.area())
print ("this triangle area is : ",triangle.area())
