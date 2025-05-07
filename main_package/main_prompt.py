from .abstract_prompt import AbstractPrompt
from .library_manager import Library

class MainMenuPrompt(AbstractPrompt):

    def __init__(self):
        super().__init__()

    def display_greeting(self):
        self.display_info_padding_top("Greetings!\n>>>> Welcome to tinyShelf2 <<<<")

    def current_prompt(self):
        while True:
            print(
                "\nWhat do you wish to do?\n" +
                "\nType:" +
                "\n(a) to add new books" +
                "\n(s) to use the search function" +
                "\n(u) to update books" +
                "\n(r) to remove books\n" +
                "\n-or-" +
                "\n(p) to print the full booklist" +
                "\n(h) for help" +
                "\n(q) to quit\n"
            )
            
            answer = input("> ")

            if answer.lower() == "a":
                new_book = NewBookPrompt()
                new_book.current_prompt()                
                continue
            elif answer.lower() == "s":
                search = SearchPrompt()
                search.current_prompt()
                continue
            elif answer.lower() == "u":
                update = UpdatePrompt()
                update.current_prompt()
                continue
            elif answer.lower() == "r":
                remove = RemovePrompt()
                remove.current_prompt()
                continue
            elif answer.lower() == "p":
                self.display_info_padding_full("This section is still under construction.")
                continue
            elif answer.lower() == "h":
                self.display_info_padding_full("This section is still under construction.")
                continue
            elif answer.lower() == "q":  
                self.display_info_padding_full("Exiting...")
                self.display_info_padding_full("See you next time!")
                break
            else:
                self.display_info_padding_full("Invalid option. Please try again.")
                continue

        self.scanner.close()
        