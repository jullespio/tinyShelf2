from .abstract_prompt import AbstractPrompt
from .book import Book

class NewBookPrompt(AbstractPrompt):

    def __init__(self):
        super().__init__()

    def current_prompt(self):
        print("Please enter the following details for the book:")

        # Prompt the user for each detail
        title = input("Title: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        year = int(input("Year of publication: "))

        # Optional fields with defaults
        isbn = self.get_input("ISBN (optional): ")
        rating = self.get_input("Rating (optional, 0-5): ")
        if rating:
            rating = float(rating)

        other_info = self.get_input("Other information (optional): ")
        
        # Booleans
        read = self.get_boolean_input("Has the book been read?", False)
        lent = self.get_boolean_input("Is the book lent?", False)

        # Create the Book object
        book = Book(
            title=title,
            author=author,
            publisher=publisher,
            year=year,
            isbn=isbn or None,
            rating=rating if rating else None,
            other_info=other_info or None,
            read=read,
            lent=lent,
            # date_created=date_created,
            # date_modified=date_modified
        )

        # Print the created book object
        print("\nCreated Book:")
        print(book)

    # MAKE THIS DO THE RIGHT THING -Julles
    if __name__ == "__main__":
        create_book()
    