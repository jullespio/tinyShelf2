"""
Trevor Amestoy
Cornell University
January, 2023
"""

# Import the helpers from the current folder "."
from .helpers import *

# Import the subpackage_module
from .subpackage import subpackage_module
from .main_menu_prompt import MainMenuPrompt

def main_module_function():
        main = MainMenuPrompt()
        main.display_greeting()
        main.current_prompt()

