def parse_input(user_input):
    """Parses user input into a command and arguments."""
    cmd, *args = user_input.lower().split()
    return cmd, *args


def add_contact(args, contacts):
    """Adds a new contact to the dictionary."""
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Updates the phone number of an existing contact."""
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found. Please add the contact first."


def show_contact(args, contacts):
    """Returns the phone number of a contact by name."""
    if len(args) != 1:
        return "Invalid command."

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all_contacts(contacts):
    """Returns all saved contacts and their phone numbers."""
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def main():
    """Runs the bot and handles user commands."""
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Invalid command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["hello", "all", "exit", "close"] and args:
            print("Invalid command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()