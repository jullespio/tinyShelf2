# abstract_prompt.py

from abc import ABC, abstractmethod  # NEW: Enables formal abstraction
from .utils import PromptCancelled

class AbstractPrompt(ABC):
    """
    Abstract base class for user input prompts.
    Provides utility methods and enforces a prompt interface.
    """

    def __init__(self):
        pass

    # NEW: Required method to be implemented by subclasses
    @abstractmethod
    def current_prompt(self):
        """
        Defines the interactive prompt logic.
        Must be implemented by any subclass.
        """
        pass

    # Utility method to safely get user input, allowing optional fields
    def get_input(self, prompt_text):
        response = input(f"{prompt_text}: ").strip()
        if response.lower() == "q":
            raise PromptCancelled()
        return response

    # Utility method to ask yes/no questions and return a boolean
    def get_boolean_input(self, prompt_text, default=False):
        default_str = "y" if default else "n"
        response = input(f"{prompt_text} (y/n) [default: {default_str}] or type 'q' to cancel: ").strip().lower()
        if response == "q":
            raise PromptCancelled()
        elif response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        return default        