from pathlib import Path


def get_cats_info(path):
    """Read cat information from a file and return a list of dictionaries."""
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

    except FileNotFoundError:
        print(f"File not found: {path}")
    except (ValueError, UnicodeError):
        print(f"Invalid data in file: {path}")
    except OSError as error:
        print(f"Error reading file: {error}")

    return cats_info


path = Path(__file__).parent / "cats.txt"
cats_info = get_cats_info(path)

print(cats_info)