'''Task 1:

numb_1 = [[2, 4,1, 5], [2,10,12], [14, 16,20]]
Check the even numbers in the list. The output should be like the following:
  n is an even number.
  n is an odd number

and so on.
'''


numb_1=[[2,4,1,5],[2,10,12],[14,16,20]]
for sublist in numb_1:
    for n in sublist:
        if n%2==0:
            print(f'{n} is an even number')
        else:
            print(f'{n} is an odd number') 

'''Write a function process_numbers(numbers, operation) that:

Takes a list of integers (numbers)

Takes an operation string ("double", "square", "cube", "filter_even", "sum")

Returns the result depending on the operation:

"double" -> return a new list with each number doubled

"square" -> return a new list with each number squared

"cube" -> return a new list with each number cubed

"filter_even" -> return a new list with only even numbers
and if there is an invalid parameter given for operation name then print invalid input.
'''
   
   
   
'''Task 3:even_numbers = [2,4,6,8]
Write a try catch block to print the fifth indexed number. 
(hint: here the 5th index is invalid. So we should get error for that. 
That's why you have write a try catch block)'''



even_numbers=[2,4,6,8]
try:
    print(even_numbers[5])
except IndexError:
    print('Error:index out of bound')  






'''Task 1 of OOP:
Create a Family object. It should have attribute such as my_name, father_name, mother_name, sister_name, brother_name
You have to create the class using a constructor. Initiate it and set values to the attributes.'''


class Family:
    def __init__(self,my_name, father_name, mother_name,sister_name, brother_name):
       self.myname = my_name
       self.fathername = father_name
       self.mothername = mother_name
       self.sistername = sister_name
       self.brothername = brother_name
family= Family("Ayesha","Amjad","Selina","Sumona","Emran")
print(f'my name: {family.myname},father name: {family.fathername}, mother name:{family.mothername}, sister name:{family.sistername}, brother:{family.brothername}')      




#Rectangle
class Rectangle():

  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    return self.length*self.width
  def perimeter(self):
    return 2*(self.length+self.width)
rectangle = Rectangle(2,4)
print(f' Rectangle Area:{rectangle.area()},Rectangle perimeter:{rectangle.perimeter()}')



#Triangle
class Triangle():
    def __init__(self,base,height,hypotenuse):
        self.base=base
        self.height=height
        self.hypotenuse=hypotenuse
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.base+self.height+self.hypotenuse
triagle=Triangle(2,4,5) 
print(f'Triangle area:{triagle.area()},Triangle perimeter:{triagle.perimeter()}')  



#square
class Square():
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
square=Square(6)
print(f'Square area:{square.area()},Square perimeter:{square.perimeter()}')                
    
  

