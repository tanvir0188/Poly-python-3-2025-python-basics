class Square:
    def __init__(self,a):
        self.a=a
    
    def area(self):
        print(f"Square Area : {self.a**2}")

    def perimeter(self):
        print(f"Square Perimeter : {4*self.a}")

    def __str__(self):
        return "Square"
s1=Square(10)
s1.area()
s1.perimeter()