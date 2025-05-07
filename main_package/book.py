import json
from datetime import datetime

class Book:
    def __init__(self, title, author, publisher, year, isbn=None,
                 rating=None, other_info=None, read=False, lent=False,
                 date_created=None, date_modified=None):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.rating = rating
        self.other_info = other_info
        self.read = read
        self.lent = lent
        self.date_created = date_created or datetime.now()
        self.date_modified = date_modified or datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.date_modified = datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "year": self.year,
            "isbn": self.isbn,
            "rating": self.rating,
            "other_info": self.other_info,
            "read": self.read,
            "lent": self.lent,
            "date_created": self.date_created.isoformat(),
            "date_modified": self.date_modified.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            publisher=data.get("publisher"),
            year=data.get("year"),
            isbn=data.get("isbn"),
            rating=data.get("rating"),
            other_info=data.get("other_info"),
            read=data.get("read", False),
            lent=data.get("lent", False),
            date_created=datetime.fromisoformat(data["date_created"]),
            date_modified=datetime.fromisoformat(data["date_modified"]),
        )

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
