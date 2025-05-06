import sys

class AbstractPrompt:

    def __init__(self):
        self.scanner = sys.stdin

    @staticmethod
    def display_info_padding_full(info_to_display):
        print(f"\n{info_to_display}\n")

    @staticmethod
    def display_info_padding_top(info_to_display):
        print(f"\n{info_to_display}")

    @staticmethod
    def display_info_padding_bottom(info_to_display):
        print(f"{info_to_display}\n")

    def continue_or_not(self):
        while True:
            print("\nContinue? [y/n]")
            answer = input("> ")
            print()
            
            if answer.lower() == "y":
                return True
            
            if answer.lower() == "n":
                return False
            
            print("\nPlease provide a valid answer.\n")
    
    def current_prompt(self):
        raise NotImplementedError("Subclasses should implement this method.")

