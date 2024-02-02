from .types import user
from .clean import clean
from .prompt import input_user
from .colors import Colors

def menu() -> user:
    """menu() is the menu main of the users."""
    clean()

    colors = Colors()

    menu_ = f"""{colors.CYAN}
----------------------------------------
Welcome to menu                        •
System-Utils functions!                •
© 2023 - あかり梓川.                   •
----------------------------------------

{colors.WHITE}[1] Convert MB's to bytes
{colors.WHITE}[2] Convert GB's to bytes
{colors.WHITE}[3] Convert TB's to bytes
{colors.WHITE}[4] Other Functions {colors.RED}[beta]
{colors.WHITE}[5] Exit"""
    print(menu_)
    option = input_user("\n⟩ ")

    if option == "":
        input("The prompt is Null... Try again.")
        return menu()

    return option
