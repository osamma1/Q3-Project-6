#Assignment:
#Create a class Book with a class variable total_books. 
#Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable to track the total number of books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Call the class method when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def display(self):
        print(f"Book Title: {self.title}")
        print(f"Total Books: {Book.total_books}")

# Example usage:
book1 = Book("The Great Gatsby")
book2 = Book("1984")
book3 = Book("To Kill a Mockingbird")

book1.display()
book2.display()
book3.display()