#If a class is a blueprint for creating objects, then a metaclass is a blueprint for creating classes.
#classes.
#A class is an instance of a metaclass.
#Metaclasses are instances of 'type'
#Why use it? 
    #1.Class registration
    #2.Code validation
    #3.Api framework:SQLAlchemy,Django
import datetime
class SimpleMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating Classes: {name}")
        print(f"Base Classes: {bases}")
        print(f"Attributes: {list(attrs.keys())}")

        attrs['created_at'] = datetime.datetime.now()
        attrs['created_by'] = 'SimpleMeta'

        return super().__new__(cls, name, bases, attrs)
    
class MyClass(metaclass=SimpleMeta):
    x = 10

    def method(self):
        return "Hello from MyClass"
print(MyClass.x)
print(MyClass.created_at)
print(MyClass.created_by)