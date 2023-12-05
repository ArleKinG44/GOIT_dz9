contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError: The key you provided does not exist."
        except ValueError:
            return "ValueError: The value you provided is not valid."
        except IndexError:
            return "IndexError: The index you provided is out of range."
    return inner


@input_error
def hello():
    return "How can I help you?"


@input_error
def add(contact_info):
    name, phone = contact_info.split()
    contacts[name] = phone
    return f"Contact {name} added"


@input_error
def change(contact_info):
    name, phone = contact_info.split()
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed."
    else:
        return f"No contact named {name} found."


@input_error
def phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return f"No contact named {name} found."


@input_error
def show_all():
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


@input_error
def good_bye():
    return "Good bye!"


def main():
    while True:
        command = input().split()
        if len(command) > 1 and command[0].lower() in ["show", "good"]:
            command[0] = ' '.join(command[:2])
            command[1:] = command[2:]
        if command[0].lower() == "hello":
            print(hello())
        elif command[0].lower() == "add":
            print(add(' '.join(command[1:])))
        elif command[0].lower() == "change":
            print(change(' '.join(command[1:])))
        elif command[0].lower() == "phone":
            print(phone(' '.join(command[1:])))
        elif command[0].lower() == "show all":
            print(show_all())
        elif command[0].lower() in ["good bye", "close", "exit"]:
            print(good_bye())
            break
        else:
            print("Unknown command, try again")


if __name__ == "__main__":
    main()
