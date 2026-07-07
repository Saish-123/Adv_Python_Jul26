#Dunder Methods : Double Underscore
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
Book1 = Book("Python 101", "Mark Davis")
Book2 = Book("Python 101", "Mark Davis")
Book3 = Book("Python 201", "Jane Smith")

#print(Book1)  # Output: Python 101 by Mark Davis
#print(repr(Book1))  # Output: Book('Python 101', 'Mark Davis
print(Book1 == Book2)  # Output: True
print(Book1 == Book3)  # Output: False
#__getitem__ : for indexing items
#__call__ : make object callable
