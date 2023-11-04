from .menu import menu
from .types import user
from .prompt import input_user
from .convert import gb_to_bytes

def options(op: user) -> user:
    """options() is the choice options of the menu()."""

    match op:

        case "1":
            print("""Function: Gibibytes to bytes.""")
            
            option = input_user("Enter gibibytes ⟩ ")

            if option == "":
                return options(op)

            result = gb_to_bytes(int(option))
            input(f"{option}gb (gibibytes) is equal the {result} bytes.")

            # back to menu.
            return options(menu())

        case "2":
            print("Bye... •́⁠ ⁠ ⁠‿⁠ ⁠,⁠•̀")

    return op
