class Book:
    def __init__(self, id, title, author, copies):
        # Store the book details
        self.id=id
        self.title=title
        self.author=author
        self.total=copies
        self.available=copies   # At first, all books are available

    def borrow_book(self):
        if self.available>0:
            self.available-=1
            print("Book borrowed successfully.")
        else:
            print("Sorry! No copies are available.")

    def return_book(self):
        if self.available<self.total:
            self.available+=1
            print("Book returned successfully.")
        else:
            print("All copies are already in the library.")

    def display_details(self):
        print("Book ID:", self.id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available Copies:", self.available, "/", self.total)


# Testing the program

book1 = Book(101, "Python Programming", "Pavan Kumar", 3)

print("Step 1: Book Details")
book1.display_details()

print("\nStep 2: Borrowing Books")
book1.borrow_book()
book1.borrow_book()

print("\nStep 3: Book Details")
book1.display_details()

print("\nStep 4: Borrowing More Books")
book1.borrow_book()
book1.borrow_book()   # This should show that no copies are left

print("\nStep 5: Returning a Book")
book1.return_book()

print("\nStep 6: Final Book Details")
book1.display_details()