# Notes. Additional functional
import os
import pickle
from collections import UserList


class Note:
    # note takes 2 parameters: text (mandatory) and tag (not obligatory)
    def __init__(self, text: str, tags: list = []):
        self.text = text
        self.tags = tags

    def __str__(self):
        return " ".join(self.tags) + " " + self.text


class Notes(UserList):
    count = 0

    def add(self, note: Note):
        self.data[self.count] = note


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError, TypeError):
            return 'Wrong input, try one more time'

    return wrapper


@input_error
def add_note(notes, args: list):
    tags_list = []
    print(args)
    for word in args:
        if word.startswith("#"):
            tags_list.append(word)
            args.remove(word)
    text = ' '.join(args)
    note = Note(text, tags_list)
    notes.data.append(note)
    return f'Note number {notes.data.index(note)} added successfully'


def find_text(notes, args: list):
    text = ' '.join(args)
    flag = 0
    result = ''
    for note in notes:
        if str(note).find(text) != -1:
            result += '{:<4}'.format(notes.data.index(note)) + str(note) + '\n'
            flag += 1
    if flag == 0:
        result = f'There are no "{text}" symbols in your notes'
    return result


def edit_note(notes, *args):
    pass


def delete_note(notes, *args):
    pass


def add_tag(notes, *args):
    pass


def sort_by_tag(notes, *args):
    pass


def show_notes(notes, *args):
    res = ""
    for note in notes.data:
        res += '{:<4}'.format(notes.data.index(note)) + str(note) + "\n"
    return res


def exit(notes, *args):
    path = 'database/notes_db.bin'
    with open(path, 'wb') as file:
        pickle.dump(notes, file)
    return f'Your notes saved in file {path}. Good bye!'


COMMANDS = {
    add_note: ("add",),
    find_text: ("find",),
    edit_note: ("edit note",),
    delete_note: ("delete note",),
    add_tag: ("add tag",),
    sort_by_tag: ("sort by tag",),
    exit: ("exit",),
    show_notes: ("show",),
}


def processing(customer_input):
    for k in COMMANDS:
        for command in COMMANDS[k]:
            if customer_input.lower().strip().startswith(command):
                list_of_data = customer_input[len(command):].strip().split(" ")
                return k, list_of_data


def main1():
    path = 'database/notes_db.bin'
    if os.path.isfile(path):
        with open(path, 'rb') as file:
            notes = pickle.load(file)
    else:
        notes = Notes()

    while True:
        customer_input = input(">>>")
        func, data = processing(customer_input)
        print(func(notes, data))
        if func == exit:
            break


if __name__ == '__main__':

    main1()
