###########################
## Messages & Formatting ##
###########################

# NEW: Visually emphasizes messages
def print_boxed_message(message):
    print("\n" + "=" * 37)
    print(message)
    print("=" * 37 + "\n")

# NEW: Adds vertical spacing to standard messages
def print_padded_message(message):
    print("\n" + message + "\n")

def display_greeting():
    # Using ANSI escape codes for text color & style
    print_boxed_message(" " * 13 + "Greetings!\n>>>> Welcome to \033[1;92mtinyShelf\033[0m (v2.0) <<<<")

########################
## Exception handling ##
########################

class PromptCancelled(Exception):
    """Raised when the user cancels the current prompt."""
    pass
