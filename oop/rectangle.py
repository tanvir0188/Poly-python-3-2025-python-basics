class Rectangle:
    def __init__(self,Length,Width):
        self.Length=Length
        self.width=Width

    def area(self):
        print(f'Rectangle Area : {self.Length*self.width}')

    def Perimeter(self):
        print(f"Rectangle Perimeter : {2 * (self.Length+self.width)}")
    def __str__(self):
        return f"  Rectangle  "

r=Rectangle(10,20)
r.area()
r.Perimeter()
