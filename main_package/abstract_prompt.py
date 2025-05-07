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

    def get_input(self, prompt, default=None):
        value = input(prompt)
        return value if value else default

    def get_boolean_input(self, prompt, default=False):
        while True:
            value = input(prompt + " (y/n): ").strip().lower()
            if value in ['y', 'yes']:
                return True
            elif value in ['n', 'no']:
                return False
            else:
                print("Invalid input, please enter 'y' or 'n'.")
    
    def current_prompt(self):
        raise NotImplementedError("Subclasses should implement this method.")

