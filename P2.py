class Animal():
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some Sound"
    
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"
    
class Cow(Animal):    
    def make_sound(self):
        return f"{self.name} says Moo!"
    
cat = Cat("Bell")
cow = Cow("Jerry")

print(cat.make_sound())
print(cow.make_sound())