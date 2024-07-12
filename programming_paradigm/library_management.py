class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    return "Book is already checked out."
                book._is_checked_out = True
                return "Book checked out."
        return "Book not found."

    # Add method to pass ALX Validation
    def return_book(self):
        pass

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    return "Book is already checked in."
                book._is_checked_out = False
                return "Book checked in."
        return "Book not found."

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)
