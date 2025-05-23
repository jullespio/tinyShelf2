# Import the helpers from the current folder "."
from tinyshelf2.utils.utils import display_greeting

# Import the subpackage_module
# from .subpackage import subpackage_module
from tinyshelf2.prompts.main_prompt import CLIMenuInterface

def main_module_function():
        main = CLIMenuInterface()
        display_greeting()
        main.current_prompt()

