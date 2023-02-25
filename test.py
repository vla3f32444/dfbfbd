from math import pi

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def doesExist(self):
        maxim = max(self.a,self.b,self.c)
        if(self.a + self.b + self.c - maxim > maxim):
            return True
        else:
            return False

circleOne = Circle(5)
print(circleOne.perimeter())
circleTwo = Circle(13443434)
print(circleTwo.perimeter())