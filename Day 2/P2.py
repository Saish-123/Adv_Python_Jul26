#Example of Abstract Base Class (ABC)
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod #decorator
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    #Concrete Method
    def description(self):
        return f"This shape has area {self.area()} and perimeter {self.perimeter()}"

#Child Class
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius  

    def area(self):
        return 3.14*self.radius**2

c = circle(5)
print("Area of Circle:", c.area())
print("Perimeter of Circle:", c.perimeter())
print(c.description())