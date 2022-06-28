import os
import pickle
import sys
import time

import keyboard
import psutil
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from address_book import address_book_functions as f
from address_book.address_book_class import AddressBook
from command_handling import handle_cmd
from notes import notes as n
from notes.notes import Notes


def main():
    mode = None
    # contacts = None
    notes = None
    arg = None  # argument to pass to `handle_cmd()` depending on the mode
    terminal_run = False  # for prompt_toolkit
    command_completer = None

    # Check if program is running PyCharm or cmd, bash, etc. for prompt_toolkit
    shells = {"cmd.exe", "bash.exe", "powershell.exe", "WindowsTerminal.exe"}
    parents = {parent.name() for parent in psutil.Process().parents()}
    if bool(parents & shells):
        terminal_run = True

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

            # Load contacts from file
            data, result = contacts.load_from()
            if not (data is None):
                contacts.data = data
            print(f"\n{result}")

            if terminal_run:
                command_completer = WordCompleter(
                    ['help', 'exit', 'hello', 'add_contact', 'remove_contact', 'change_phone', 'remove_phone',
                     'show_email', 'change_email', 'remove_email', 'show_phones', 'show_all', 'edit_birthday',
                     'days_to_birthday' 'birthday_in', 'save', 'load', 'find_contact'])

        if keyboard.is_pressed('2'):
            input()
            mode = 'Notes'

            path = 'database/notes_db.bin'
            if os.path.isfile(path):
                with open(path, 'rb') as file:
                    notes = pickle.load(file)
                print(f"\nNotes have been loaded from '{path}' successfully!")
            else:
                notes = Notes()
            arg = notes

            print("\nMode: Notes")

        if keyboard.is_pressed('3'):
            input()
            mode = 'Sorting'
            print("\nMode: Sorting")

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
        print()


if __name__ == '__main__':
    main()
