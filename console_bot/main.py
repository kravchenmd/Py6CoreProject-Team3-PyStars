import os
import pickle
import sys
import time
from importlib.resources import files

import keyboard
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from console_bot.address_book import address_book_functions as f
from console_bot.address_book.address_book_class import AddressBook
from console_bot.command_handling import handle_cmd
from console_bot.notes import notes_class as n
from console_bot.notes.notes_class import Notes


# if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
#     # Script from terminal
#     print(1)
#     # import console_bot
#     from address_book import address_book_functions as f
#     from notes import notes_class
#     from notes import notes_class as n
#     from address_book.address_book_class import AddressBook
#     from notes.notes_class import Notes
#     from command_handling import handle_cmd
# else:


def main():
    mode = None
    # contacts = None
    # notes = None
    arg = None  # argument to pass to `handle_cmd()` depending on the mode
    terminal_run = False  # for prompt_toolkit
    command_completer = None

    # # Check if program is running PyCharm or cmd, bash, etc. for prompt_toolkit
    # shells = {"cmd.exe", "bash.exe", "powershell.exe", "WindowsTerminal.exe"}
    # parents = {parent.name() for parent in psutil.Process().parents()}
    # if bool(parents & shells):
    #     terminal_run = True
    # print(terminal_run)

    start_message = "*** Console bot project ***\n" \
                    "***  Team #3 - PyStars  ***\n"
    print(start_message)
    time.sleep(1)
    start_message = "Modes of the bot:\n" \
                    "\tEsc - Exit\n" \
                    "\t1   - Address book mode\n" \
                    "\t2   - Note mode\n" \
                    "\t3   - Sorting of a folder\n" \
                    "Input number and press Enter, or press Esc to exit..."
    print(start_message)

    while not mode:
        if keyboard.is_pressed('Esc'):
            print("\nGoodbye!")
            sys.exit()  # exit program (to prevent going to the next while)

        if keyboard.is_pressed('1'):
            input()
            mode = 'AddressBook'
            contacts = AddressBook()
            arg = contacts

            # Load contacts from file
            data, result = contacts.load_from()
            if not (data is None):
                contacts.data = data
            print(f"\n{result}")

            # TODO: add the same to mode of Notes and Sorting
            if terminal_run:
                command_completer = WordCompleter(
                    ['help', 'exit', 'hello', 'add_contact', 'remove_contact', 'change_phone', 'remove_phone',
                     'show_email', 'change_email', 'remove_email', 'show_phones', 'show_all', 'edit_birthday',
                     'days_to_birthday' 'birthday_in', 'save', 'load', 'find_contact', 'back'])

        if keyboard.is_pressed('2'):
            input()
            mode = 'Notes'

            my_resources = files('console_bot')
            path = str(my_resources / 'database/notes_db.bin')

            if os.path.isfile(path):
                with open(path, 'rb') as file:
                    notes = pickle.load(file)
                print(f"\nNotes have been loaded from '{path}' successfully!")
            else:
                notes = Notes()
            arg = notes

            print("\nMode: Notes")
            if terminal_run:
                command_completer = WordCompleter(
                    ['help', 'exit', 'back', 'hello', 'add', 'find', 'edit', 'delete',
                     'show', 'new tag', 'sort by tag'])

        if keyboard.is_pressed('3'):
            input()
            mode = 'Sorting'
            print("\nMode: Sorting")

            if terminal_run:
                command_completer = WordCompleter(
                    ['help', 'back', 'close', 'exit', 'goodbye', 'sort_folder'])

    print("***For help type `help` command**\n")

    while True:
        # text = prompt('Enter HTML: ', completer=html_completer)
        command = None

        if terminal_run:
            command = prompt('Enter command: ', completer=command_completer)
        while not command:
            command = input('Enter command: ')

        func, result = handle_cmd(command, arg, mode)

        if mode == 'Notes':
            print(func(notes, result))
        else:
            print(result)

        if func == f.exit_program or func == n.exit_notes:
            break
        elif func == f.back:
            main()
        print()


if __name__ == '__main__':
    main()
