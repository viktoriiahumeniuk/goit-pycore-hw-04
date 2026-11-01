import sys
from pathlib import Path
from colorama import Fore, Style


def show_directory(path, level=0):
    """Display files and directories recursively with colors."""
    for item in path.iterdir():
        indent = "    " * level

        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            show_directory(item, level + 1)
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    """Validate the path and display the directory structure."""
    if len(sys.argv) != 2:
        print("Usage: python task3.py <directory_path>")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"Error: Path does not exist: {path}")
        return

    if not path.is_dir():
        print(f"Error: Not a directory: {path}")
        return

    try:
        print(f"{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
        show_directory(path)

    except PermissionError:
        print("Error: Permission denied")
    except OSError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()