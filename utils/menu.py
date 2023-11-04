from .types import user
from .clean import clean
from .prompt import input_user

def menu() -> user:
    """menu() is the menu main of the users."""
    clean()
    menu_ = """
----------------------------------------
Welcome to menu                        •
of the system utils functions.         •
© 2023 - あかり梓川.                   •
----------------------------------------

[1] Convert GB's to bytes
[2] Exit Program"""
    print(menu_)

    option = input_user("\n⟩ ")

    if option == "":
        input("The prompt is Null... Try again.")
        return menu()

    return option
