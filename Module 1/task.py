
class Rectangle:
     def __int__ (self,width,height):
         self.width= width
         self.height= height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle=Rectangle(4,5)   
print(f'regtangle length: {rectangle.length}, rectangle width: {rectangle.width}, rectangle area: {rectangle.area()}, rectangle perimeter: {rectangle.perimeter()}')


class Squre:
    def __int__ (self,side):
        self.side=side
    
    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

square=Squre(4)
print(f'side {square.side}, square area {square.area()}, square perimeter {square.perimeter()}')


class Triangle:
    def __int__(self,base,height):
       self.base= base
       self.height= height

    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        