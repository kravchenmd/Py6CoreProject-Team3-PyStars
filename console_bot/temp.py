from collections import UserDict
from typing import List, Tuple

exit_commands = ('good bye', 'close', 'exit')
contacts = {}


class Field:
    pass


class Name(Field):
    def __init__(self, name: str) -> None:
        self.name = name


class Phone(Field):
    def __init__(self, phone: str) -> None:
        self.phone = phone


class Record:
    def __init__(self, name: Name) -> None:
        self.name: Name = ''
        self.phone_list: List[Phone] = []

    def add_phone(self, phone: Phone) -> None:
        if phone in self.phone_list:
            print(f"Name '{name}' is already in contacts!")
            print("Try another name or change existing contact")
            return

        self.phone.append(phone)
        print(f'Phone was added successfully!')

    def remove_phone(self, phone: Phone) -> None:
        if phone in self.phone_list:
            self.phone_list.remove(phone)
            print(f'Phone was removed successfully!')
            return
        print(f"Phone can't be removed: it's not in the list!")

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        if phone in self.phone_list:
            self.phone_list.remove(phone)
            self.phone_list.append(new_phone)
            print(f'Phone was edited successfully!')
            return
        print(f"Phone can't be edited: it's not in the list!")


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        # self.contacts = {}



    def change_contact(self, name: str, phone: str) -> None:
        if name in self.contacts.keys():
            self.contacts[name] = phone
            print(f'Contact was changed successfully!')
            return
        print(f"Contact can't be changed: it's not in the list!")

        if name not in contacts.keys():
            print(f"There is no contact with name '{name}'")
            return

        contacts.update({name: phone})
        print(f'Contact was updated successfully!')




# This decorator handles correctness of the phone number: can start with '+'
# and then must contain only digits. But doesn't check if the number is real
def input_error(func):
    def wrapper(*args):
        if len(args) != 2:
            return func(*args)

        name, phone = args
        try:
            phone_check = phone[1:] if phone[0] == '+' else phone
            # check at once if the phone number doesn't start with '-' sign
            # and if it contains only digits by int()
            if int(phone_check) < 0:
                raise ValueError
        except ValueError:
            print("ERROR: Phone can or couldn't start with '+' and then must contain only digits!")
            print("Example: +380..., 380...")
            return

        result = func(name, phone)
        return result

    return wrapper


# This decorator handles the correct number of arguments that are passed into the function
def func_arg_error(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            f_name = func.__name__
            if f_name in ('hello', 'show_all_phones'):
                print("ERROR: This command has to be written without arguments!")
            if f_name in ('add_phone', 'change_phone'):
                print("ERROR: This command needs 2 arguments: 'name' and 'phone' separated by 1 space!")
            if f_name == 'show_phone':
                print("ERROR: This command needs 1 arguments: 'name' separated by 1 space!")

    return wrapper


@func_arg_error
def hello() -> None:
    print("Hello! How can I help you?")


# @input_error
# @func_arg_error
# def add_phone(name: str, phone: str) -> None:
#     if name in contacts.keys():
#         print(f"Name '{name}' is already in contacts!")
#         print("Try another name or change existing contact")
#         return
#
#     contacts.update({name: phone})
#     print(f'Contact was added successfully!')


@input_error
@func_arg_error
def change_phone(name: str, phone: str):
    if name not in contacts.keys():
        print(f"There is no contact with name '{name}'")
        return

    contacts.update({name: phone})
    print(f'Contact was updated successfully!')


@func_arg_error
def show_phone(name: str) -> None:
    if name not in contacts.keys():
        print(f"There is no contact with name '{name}'")
        return

    print(contacts.get(name))


@func_arg_error
def show_all_phones() -> None:
    if not contacts:
        print("There are no contacts to show yet...")
        return

    for name, phone in contacts.items():
        print(name, phone)


def choose_command(cmd: list):
    cmd_check = cmd[0].lower()

    if cmd_check == 'hello':
        return hello
    if cmd_check == 'add':
        return add_phone
    if cmd_check == 'change':
        return change_phone
    if cmd_check == 'phone':
        return show_phone
    if cmd_check == 'show':
        # take into account that this command consists 2 words
        cmd[:2] = [' '.join(cmd[:2])]
        cmd_check = cmd[0].lower()
        if cmd_check == 'show all':
            return show_all_phones

    print('Unknown command')
    return None


def parse_command(cmd: str):
    cmd = cmd.strip().split(' ')  # apply strip() as well to exclude spaces at the ends
    func = choose_command(cmd)
    if func:
        func(*cmd[1:]) if len(cmd) > 1 else func()  # else part to take into account hello() and show()


def main():
    while True:
        command = None

        # Check if command is not empty
        while not command:
            command = input('Enter command: ')

        if command in exit_commands:
            print("Good bye!")
            break

        func, result = parse_command(command)

        print(result)

        if func == exit_program:
            break
        print()


if __name__ == '__main__':
    main()
