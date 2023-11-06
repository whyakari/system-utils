from .menu import menu
from .types import user
from .prompt import input_user
from .convert import gb_to_bytes, mb_to_bytes, tb_to_bytes

def options(op: user) -> user:
    """options() is the choice options of the menu()."""

    match op:

        case "1":
            print("""Function: Megabytes to bytes""")

            option = input_user("Enter megabytes ⟩ ")

            if option == "":
                return options(op)

            result = mb_to_bytes(int(option))
            input(f"{option}MB (megabytes) is equal the {result} bytes.")

            return options(menu())

        case "2":
            print("""Function: Gibibytes to bytes.""")
            
            option = input_user("Enter gibibytes ⟩ ")

            if option == "":
                return options(op)

            result = gb_to_bytes(int(option))
            input(f"{option}GB (gibibytes) is equal the {result} bytes.")

            # back to menu.
            return options(menu())

        case "3":
            print("""Function: Terabytes to bytes""")

            option = input_user("Enter terabytes ⟩ ")

            if option == "":
                return options(op)

            result = tb_to_bytes(int(option))
            input(f"{option}TB (terabytes) is equal the {result} bytes.")

            return options(menu())

        case "4":
            print("Bye... •́⁠ ⁠ ⁠‿⁠ ⁠,⁠•̀")

    return op
