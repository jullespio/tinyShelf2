import json
from .book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, **kwargs):
        new_book = Book(title, author, **kwargs)
        self.books.append(new_book)
        return new_book

    def list_books(self):
        return self.books

    def find_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def delete_book_by_isbn(self, isbn):
        before = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        return len(self.books) < before

    def delete_book_by_title(self, title):
        before = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        return len(self.books) < before

    def export_to_file(self, filepath):
        with open(filepath, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f, indent=2)

    def import_from_file(self, filepath):
        with open(filepath, 'r') as f:
            book_data_list = json.load(f)
            self.books = [Book.from_dict(data) for data in book_data_list]
