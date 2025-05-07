from datetime import datetime

class Book:
    def __init__(self, title, author, publisher, year, isbn=None,
                 rating=None, other_info=None, read=False, lent=False):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.rating = rating  # e.g., a float or int (0-5)
        self.other_info = other_info  # any additional information
        self.read = read
        self.lent = lent
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

    # The method below updates an object's attributes using keyword arguments, only if those 
    # attributes already exist, and then sets a date_modified attribute to the current time.

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.date_modified = datetime.now()

    def __repr__(self):
        return (f"Book(title='{self.title}', author='{self.author}', "
                f"publisher='{self.publisher}', year={self.year}, isbn='{self.isbn}', "
                f"rating={self.rating}, read={self.read}, lent={self.lent}, "
                f"date_created={self.date_created}, date_modified={self.date_modified})")
