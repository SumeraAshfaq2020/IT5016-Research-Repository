# Simple Library Management System
# This program demonstrates basic OOP concepts


# Book class
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


# Member class
class Member:

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# Library class
class Library:

    def __init__(self):
        self.books = []
        self.members = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)

    # Add a member
    def add_member(self, member):
        self.members.append(member)

    # Borrow a book
    def borrow_book(self, member, book):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print("Book borrowed:", book.title)
        else:
            print("Book is not available.")

    # Return a book
    def return_book(self, member, book):
        book.available = True
        member.borrowed_books.remove(book)
        print("Book returned:", book.title)

    # Display books
    def display_books(self):
        print("\n Library Books ")

        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)

            if book.available:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            print("")


# Creating objects
library = Library()

book1 = Book("Python Basics", "John Smith")
book2 = Book("Programming Basics", "Mary Jones")

member1 = Member("Sana")


# Adding books and member
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)


# Display books
library.display_books()

# Borrow a book
library.borrow_book(member1, book1)

# Display books again
library.display_books()

# Return the book
library.return_book(member1, book1)

# Display books again
library.display_books()
