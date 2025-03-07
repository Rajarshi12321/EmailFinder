import sys
import os

# Try to import and initialize Colorama for Windows compatibility.
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    # Fallback: check if sys.stdout is a tty (which might support ANSI escapes)
    COLOR_ENABLED = sys.stdout.isatty()


def print_error(msg, start="", end=""):
    prefix = f"{start}[!] "
    if COLOR_ENABLED:
        # Use ANSI escape sequences for red
        # If Colorama is available, Fore.RED and Style.RESET_ALL will be defined.
        red = Fore.RED if "Fore" in globals() else "\033[91m"
        reset = Style.RESET_ALL if "Style" in globals() else "\033[0m"
        print(f"{red}{prefix}{reset}{msg}{end}")
    else:
        print(f"{prefix}{msg}{end}")


def print_ok(msg, start="", end=""):
    prefix = f"{start}[+] "
    if COLOR_ENABLED:
        green = Fore.GREEN if "Fore" in globals() else "\033[92m"
        reset = Style.RESET_ALL if "Style" in globals() else "\033[0m"
        print(f"{green}{prefix}{reset}{msg}{end}")
    else:
        print(f"{prefix}{msg}{end}")


def print_info(msg, start="", end=""):
    prefix = f"{start}[i] "
    if COLOR_ENABLED:
        yellow = Fore.YELLOW if "Fore" in globals() else "\033[93m"
        reset = Style.RESET_ALL if "Style" in globals() else "\033[0m"
        print(f"{yellow}{prefix}{reset}{msg}{end}")
    else:
        print(f"{prefix}{msg}{end}")


# Example usage:
if __name__ == "__main__":
    print_error("This is an error message.")
    print_ok("This is a success message.")
    print_info("This is an informational message.")
