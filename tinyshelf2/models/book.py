from datetime import datetime  # Used to track creation and modification times

class Book:
    def __init__(self, title, author, publisher, year, date_created, date_modified, isbn=None,
             rating=None, other_info=None, read=False, lent=False,
             ):

        # Ensure title, author, and publisher are non-empty strings
        for field_name, field_value in [("title", title), ("author", author), ("publisher", publisher)]:
            if not isinstance(field_value, str) or not field_value.strip():
                raise ValueError(f"{field_name.capitalize()} must be a non-empty string.")

        # Validate that year is an integer within a reasonable range
        if not isinstance(year, int) or not (1450 <= year <= datetime.now().year + 1):
            raise ValueError("Year must be a valid integer between 1450 and next year.")

        # Validate that rating (if provided) is a number between 0 and 5
        if rating is not None:
            if not isinstance(rating, (int, float)) or not (0 <= rating <= 5):
                raise ValueError("Rating must be a number between 0 and 5.")

        # Ensure ISBN is a string if provided
        if isbn is not None and not isinstance(isbn, str):
            raise ValueError("ISBN must be a string.")

        # Store the provided data in the object's attributes
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.rating = rating
        self.other_info = other_info
        self.read = read
        self.lent = lent
        self.date_created = datetime.now()  # Set creation time
        self.date_modified = datetime.now()  # Set modification time

    def update(self, **kwargs):
        # Update existing attributes with provided values
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.date_modified = datetime.now()  # Update the modification timestamp

    def to_dict(self):
        # Convert object attributes to a dictionary for saving/exporting
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
        # Recreate a Book object from a dictionary (e.g., when loading from a file)
        return cls(
            title=data["title"],
            author=data["author"],
            publisher=data["publisher"],
            year=data["year"],
            isbn=data.get("isbn"),
            rating=data.get("rating"),
            other_info=data.get("other_info"),
            read=data.get("read", False),
            lent=data.get("lent", False),
            date_created=datetime.fromisoformat(data["date_created"]),
            date_modified=datetime.fromisoformat(data["date_modified"]),
        )

    def __repr__(self):
        # Return a simple string representation of the book
        return f"Book(title='{self.title}', author='{self.author}')"
