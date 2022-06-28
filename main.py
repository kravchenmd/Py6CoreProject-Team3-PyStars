import msvcrt
import os
import pickle
import sys
import time

import functions as f
import notes as n
from classes import AddressBook
from notes import Notes, Note
from command_handling import handle_cmd


def main():
    mode = None
    contacts = None
    notes = None
    arg = None  # argument to pass to `handle_cmd()` depending on the mode

    start_message = "*** Console bot project ***\n" \
                    "***  Team #3 - PyStars  ***\n"
    print(start_message)
    time.sleep(1)
    start_message = "Modes of the bot:\n" \
                    "\t0. Exit\n" \
                    "\t1. Address book mode\n" \
                    "\t2. Note mode\n" \
                    "\t3. Sorting of a folder\n" \
                    "Press needed number..."
    print(start_message)

    while not mode:
        if msvcrt.kbhit():  # if key is pressed
            key_code = ord(msvcrt.getche())  # get ASCII code of pressed key0
            match key_code:
                case 48:  # 0 - Exit
                    print("\nGoodbye!")
                    sys.exit()  # exit program (to prevent going to the next while)
                case 49:  # 1 - Address book
                    mode = 'AddressBook'
                    print("\nAddress book mode")
                case 50:  # 2 - Note
                    mode = 'Notes'
                    print("\nNotes mode")
                case 51:  # 3 - Sorting
                    mode = 'Sorting'
                    print("\nSorting mode")

    if mode == 'AddressBook':
        contacts = AddressBook()
        arg = contacts
        # Load contacts from file
        data, result = contacts.load_from()
        if not (data is None):
            contacts.data = data
        print(result)

    # TODO Larisa: Initialization of Notes
    # Просто пледложение по аналогии с AddressBook. Можно попробовать сделать по-другому
    if mode == 'Notes':
        path = 'database/notes_db.bin'
        if os.path.isfile(path):
            with open(path, 'rb') as file:
                notes = pickle.load(file)
            print(f"Notes have been loaded from '{path}' successfully!")
        else:
            notes = Notes()
        arg = notes

    print("\n***For help type `help` command**\n")

    while True:
        command = None
        # Check if command is not empty
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
