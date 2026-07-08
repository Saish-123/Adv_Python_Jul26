#Abstract Base Class (ABCs)
#Dominos Pizza Company(ABC)

    #Templates:
        #How the Interiors
        #What SHould Be Your Menu
        #Ingridients To Be Used
        #uniform/dress code for the employees

#Example without ABC
        
class shape():
    def area(self):
        pass

    def perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius  

    def area(self):
        return 3.14*self.radius**2

class = circle(5)
print("Area of Circle:", c.area())