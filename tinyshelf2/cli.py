"""
This script is the main executable, calling the main_module_function which does
the rest of the work.
"""

# Import the main package
from tinyshelf2 import main_package

def run():
    prompt = main_package.main_module_function()
    return prompt

# Run the function if this is the main file executed
if __name__ == "__main__":
    run()
