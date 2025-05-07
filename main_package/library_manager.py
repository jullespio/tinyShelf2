from book import Book
import json  # Used to handle exporting and importing books as JSON

class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, title, author, publisher, year, **kwargs):
        # Check if the book's ISBN already exists to prevent duplicates
        isbn = kwargs.get("isbn")
        if isbn and self._isbn_exists(isbn):
            raise ValueError(f"A book with ISBN {isbn} already exists.")
        
        # Create a new Book object and add it to the library
        new_book = Book(title, author, publisher, year, **kwargs)
        self.books.append(new_book)
        return new_book

    def _isbn_exists(self, isbn):
        # Check if the given ISBN already exists in the library's books list
        return any(book.isbn == isbn for book in self.books if book.isbn)

    def list_books(self):
        # Return the list of books in the library
        return self.books

    def find_books_by_title(self, title):
        # Search for books by title (case-insensitive)
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author):
        # Search for books by author (case-insensitive)
        return [book for book in self.books if author.lower() in book.author.lower()]

    def delete_book_by_isbn(self, isbn):
        # Delete a book from the library using its ISBN (returns True if deleted)
        before = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        return len(self.books) < before

    def delete_book_by_title(self, title):
        # Delete a book from the library using its title (returns True if deleted)
        before = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        return len(self.books) < before

    def export_to_file(self, filepath):
        # Save the current list of books to a file in JSON format
        with open(filepath, 'w') as f:
            # Convert each book to a dictionary and write it to the file
            json.dump([book.to_dict() for book in self.books], f, indent=2)

    def import_from_file(self, filepath):
        # Load books from a JSON file into the library
        with open(filepath, 'r') as f:
            # Read the JSON data and recreate Book objects from it
            book_data_list = json.load(f)
            self.books = [Book.from_dict(data) for data in book_data_list]

    def mark_as_read(self, isbn=None, title=None):
        # Mark a book as read using either its ISBN or title
        book = self._find_single_book(isbn, title)
        if book:
            book.update(read=True)  # Update the book's 'read' status
            return True
        return False

    def mark_as_lent(self, isbn=None, title=None):
        # Mark a book as lent using either its ISBN or title
        book = self._find_single_book(isbn, title)
        if book:
            book.update(lent=True)  # Update the book's 'lent' status
            return True
        return False

    def _find_single_book(self, isbn=None, title=None):
        # Find a single book by either ISBN or title (returns None if not found)
        for book in self.books:
            if isbn and book.isbn == isbn:
                return book
            if title and book.title.lower() == title.lower():
                return book
        return None

    def sort_books(self, by="title", descending=False):
        # Sort the books in the library by a specific attribute (title, author, year, rating)
        valid_keys = {"title", "author", "year", "rating"}
        if by not in valid_keys:
            raise ValueError(f"Cannot sort by '{by}'. Must be one of {valid_keys}.")
        # Sort based on the provided attribute (ascending or descending order)
        self.books.sort(key=lambda book: getattr(book, by) or "", reverse=descending)
