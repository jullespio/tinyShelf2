from .abstract_prompt import AbstractPrompt
from .crud_prompts import NewBookPrompt, SearchPrompt, UpdatePrompt
from .utils import *

# Optional future imports (placeholders)
# from .search_prompt import SearchPrompt
# from .update_prompt import UpdatePrompt
# from .remove_prompt import RemovePrompt

# NEW: Handles the logic behind the menu choices
class MainMenuLogic:
    """
    Encapsulates the command handling logic for the main menu.
    This class contains no user input/output code.
    """

    def __init__(self):
        # Mapping from command keys to (description, handler method)
        self.commands = {
            "a": ("Add new books", self.add_book),
            "s": ("Search books", self.search_books),
            "u": ("Update a book", self.update_book),
            "r": ("Remove a book", self.remove_book),
            "p": ("Print book list", self.print_books),
            "h": ("Help", self.help),
            "q": ("Quit", self.quit),
        }
        self.quit_requested = False

    def handle_choice(self, choice):
        """
        Dispatches the appropriate method based on user input.
        """
        action = self.commands.get(choice.lower())
        if action:
            return action[1]()  # Execute handler
        else:
            return "invalid"

    # --- Command handlers ---

    def add_book(self):
        prompt = NewBookPrompt()
        prompt.current_prompt()

    def search_books(self):
        prompt = SearchPrompt()
        prompt.current_prompt()

    def update_book(self):
        prompt = UpdatePrompt()
        prompt.current_prompt()

    def remove_book(self):
        print("[Remove feature under construction]")
        # prompt = RemovePrompt()
        # prompt.current_prompt()

    def print_books(self):
        print("[Print feature under construction]")

    def help(self):
        print("Help: Choose an option to perform a specific action on your library.")

    def quit(self):
        self.quit_requested = True
        print_padded_message("Exiting... See you next time!")


# NEW: CLI-based interface that uses MainMenuLogic
class CLIMenuInterface(AbstractPrompt):
    """
    Handles input/output for the main menu via CLI.
    Interacts with MainMenuLogic to process user choices.
    """

    def __init__(self):
        super().__init__()
        self.logic = MainMenuLogic()

    def current_prompt(self):

        while not self.logic.quit_requested:
            print(
                "\nWhat do you wish to do?\n" +
                "\nType:"
            )
            for key, (desc, _) in self.logic.commands.items():
                print(f"({key}) {desc}")

            choice = input("\n> ").strip()
            result = self.logic.handle_choice(choice)

            if result == "invalid":
                print("- \033[1;31mWarning\033[0m - Invalid option. Please try again.\n")

        # Any cleanup logic could go here


# Entry point
if __name__ == "__main__":
    menu = CLIMenuInterface()
    menu.current_prompt()
