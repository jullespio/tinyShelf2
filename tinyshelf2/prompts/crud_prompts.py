from .abstract_prompt import AbstractPrompt
from .book import Book
from .library_manager import Library, get_library_filepath, add_book_and_save
from  .utils import *
from datetime import datetime

class NewBookPrompt(AbstractPrompt):
    def __init__(self):
        super().__init__()

    def current_prompt(self):
        try:
            print("Please enter book details as asked below. Type 'q' to return to main menu.")
            
            title = self.get_input("Title")
            author = self.get_input("Author")
            publisher = self.get_input("Publisher")
            year = int(self.get_input("Year of publication"))

            isbn = self.get_input("ISBN (optional)")
            rating = self.get_input("Rating (optional, 0–5)")
            if rating:
                rating = float(rating)

            other_info = self.get_input("Other information (optional)")
            read = self.get_boolean_input("Has the book been read?", False)
            lent = self.get_boolean_input("Is the book lent?", False)

            now = datetime.now()
            book_data = {
                "title": title,
                "author": author,
                "publisher": publisher,
                "year": year,
                "isbn": isbn or None,
                "rating": rating if rating else None,
                "other_info": other_info or None,
                "read": read,
                "lent": lent,
                "date_created": now,
                "date_modified": now,
            }

            library = Library()
            filepath = get_library_filepath()
            add_book_and_save(library, filepath, **book_data)

            print("\nBook successfully added and saved.")
            print(Book(**book_data))

        except PromptCancelled:
            print_padded_message("- \033[33mOperation cancelled by user. Returning to main menu...\033[0m -")
        except ValueError as e:
            print(f"\033[31mError:\033[0m {e}")


class SearchPrompt(AbstractPrompt):
    def __init__(self):
        super().__init__()

    def current_prompt(self):
        try:
            filepath = get_library_filepath()
            library = Library()
            library.import_from_file(filepath)

            search_query = self.get_input("Enter title or author to search (or type 'q' to cancel)")

            by_title = library.find_books_by_title(search_query)
            by_author = library.find_books_by_author(search_query)

            results = {book for book in by_title + by_author}

            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"• {book}")
            else:
                print("No books found matching the query.")

        except PromptCancelled:
            print_padded_message("- \033[33mSearch cancelled. Returning to main menu...\033[0m -")

class UpdatePrompt(AbstractPrompt):
    def __init__(self):
        super().__init__()

    def current_prompt(self):
        try:
            filepath = get_library_filepath()
            library = Library()
            library.import_from_file(filepath)

            identifier = self.get_input("Enter the book's title or ISBN to update")
            book = library._find_single_book(isbn=identifier, title=identifier)

            if not book:
                print("\033[31mBook not found.\033[0m")
                return

            print(f"\nCurrent info:\n{book}\n")
            print("Leave any field empty to keep the current value.")

            # Gather updated values
            title = self.get_input("New Title") or book.title
            author = self.get_input("New Author") or book.author
            publisher = self.get_input("New Publisher") or book.publisher
            year_input = self.get_input("New Year")
            year = int(year_input) if year_input else book.year

            isbn = self.get_input("New ISBN") or book.isbn
            rating_input = self.get_input("New Rating (0-5)")
            rating = float(rating_input) if rating_input else book.rating
            other_info = self.get_input("Other Info") or book.other_info

            read = self.get_boolean_input("Has the book been read?", book.read)
            lent = self.get_boolean_input("Is the book lent?", book.lent)

            # Apply updates
            book.update(
                title=title,
                author=author,
                publisher=publisher,
                year=year,
                isbn=isbn,
                rating=rating,
                other_info=other_info,
                read=read,
                lent=lent,
            )

            library.export_to_file(filepath)
            print("\n\033[32mBook updated successfully.\033[0m")
            print(book)

        except PromptCancelled:
            print_padded_message("- \033[33mUpdate cancelled. Returning to main menu...\033[0m -")
        except ValueError as e:
            print(f"\033[31mError:\033[0m {e}")

# if __name__ == "__main__":
#     prompt = NewBookPrompt()
#     prompt.current_prompt()