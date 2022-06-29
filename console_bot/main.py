import keyboard
import os
import pickle
import sys
import time

from address_book import address_book_functions as f
from notes import notes as n
from address_book.address_book_class import AddressBook
from notes.notes import Notes
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
        if keyboard.is_pressed('Esc'):
            print("\nGoodbye!")
            sys.exit()  # exit program (to prevent going to the next while)
        if keyboard.is_pressed('1'):
            mode = 'AddressBook'
            contacts = AddressBook()
            arg = contacts

            # Load contacts from file
            data, result = contacts.load_from()
            if not (data is None):
                contacts.data = data
            print(f"\n{result}")

            print("\nMode: Address book")

        if keyboard.is_pressed('2'):
            mode = 'Notes'

            path = '../database/notes_db.bin'
            if os.path.isfile(path):
                with open(path, 'rb') as file:
                    notes = pickle.load(file)
                print(f"\nNotes have been loaded from '{path}' successfully!")
            else:
                notes = Notes()
            arg = notes

            print("\nMode: Notes")

        if keyboard.is_pressed('3'):
            mode = 'Sorting'
            print("\nMode: Sorting")

    print("***For help type `help` command**\n")

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
