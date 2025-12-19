from math import pi
class Shape:
    def area(self):
        return "Area of the shape"

class Rectangle(Shape):
    def __init__(self, b, w):
        self.w = w
        self.b = b
    
    def area(self):
        return self.b * self.w

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return pi * self.rad * self.rad

    def __repr__(self):
        return f"The circle of radius {self.rad}"


def area_of_shape(shape):
    print(shape.area())


c = Circle(5)
area_of_shape(c)

r = Rectangle(3,4)
area_of_shape(r)

print(c)
