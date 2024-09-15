from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def describe(self):
        return "This is a shape"
    
class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
    def describe(self):
        return "This is a rectangle"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius**2
    def describe(self):
        return "This is a circle"
    
rect1 = Rectangle(10,20)
print(rect1.area())
print(rect1.describe())

circle1 = Circle(10)
print(circle1.area())
print(circle1.describe())