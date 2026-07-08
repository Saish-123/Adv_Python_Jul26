#Descriptors
#Security guard:
#Entrance: Check Id
#Is The Id Valid : Validation
#Access cntrol : Allowed / Not Allowed
#Log: Purpose of visit
#Exit: check

#Descriptor is like a security guard, but for your class attributes

class PositiveNumber:
    """"
        Descriptor which ensures the assigned value is a positive number.
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be a positive number.")
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.name]
        raise AttributeError(f"Can't delete {self.name}")
    
class Product:
    price = PositiveNumber()
    stock = PositiveNumber()

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

product = Product("Laptop", 50000, 10)
print(f"Product:{product.name}, Price:{product.price}, Stock: {product.stock}")

try:
    product.price = -50000  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e} ")