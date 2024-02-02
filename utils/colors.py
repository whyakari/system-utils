class Colors:
    RESET = '\033[0m'
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;37m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"

    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{Colors.RESET}"

