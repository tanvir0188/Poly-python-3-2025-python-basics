class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        print(f"triangle Area : {(1/2)*(self.base*self.height):.2f}")

    def perimeter(self):
        import math
        hypotenuse=math.sqrt(self.base**2 + self.height**2)
        print(f"Triangle Perimeter : {self.base+self.height+hypotenuse:.2f}")

    def __str__(self):
        return f"    Triangle   "
    

t1=Triangle(10,20)
t1.area()
t1.perimeter()
