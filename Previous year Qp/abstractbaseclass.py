from abc import ABC
from math import pi

class Shape(ABC):
    def area(self):
        pass

    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def circumference(self):
        return 2 * (self.length + self.width)

circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Circumference:", rectangle.circumference())
