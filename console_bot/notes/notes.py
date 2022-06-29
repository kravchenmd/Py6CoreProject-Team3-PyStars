# Notes. Additional functional
import os
import pickle
from collections import UserList


class Note:
    # note takes 2 parameters: text (mandatory) and tag (not obligatory)
    def __init__(self, text: str, tags: list | None = None):
        self.text = text
        self.tags = [] if tags is None else tags  # to exclude the issue with mutable objects
        self.tags.sort() #to store sorted tags

    def __str__(self):
        return " ".join(self.tags) + " " + self.text

    # function to compare instances of Note (>)
    def __gt__(self, other):
        res = True
        if len(self.tags) == 0:
            res = False
        elif len(other.tags) == 0:
            res = True
        else:
            res = self.tags[0] > other.tags[0]
        return res


class Notes(UserList):

    def add(self, note: Note):
        self.data.append(note)


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
    for word in args:
        if word.startswith("#"):
            tags_list.append(word)
            args.remove(word)
    text = ' '.join(args)
    note = Note(text, tags_list)
    notes.data.append(note)
    return f'Note number {notes.data.index(note)} added successfully'


@input_error
def find_text(notes, args: list):
    text = ' '.join(args)
    flag = 0
    result = ''
    for note in notes:
        if str(note).find(text) != -1:
            result += '{:<4}'.format(notes.data.index(note)) + str(note) + '\n'
            flag += 1
    if flag == 0:
        result = f'There are no "{text}" symbols in the notes'
    return result


# TODO 1 (Lara): change signature to `def edit_note(notes, note_number, *args)`
# to exclude args with two indexes (args[0][0])
# Lara: the issue is function can take only 2 arguments, not 3. And the second one is list
@input_error
def edit_note(notes, *args):
    note_number = int(args[0][0])
    words_list = args[0][1:]
    tags_list = []
    for word in words_list:
        if word.startswith("#"):
            tags_list.append(word)
            words_list.remove(word)
    text = ' '.join(words_list)
    note = Note(text, tags_list)
    if note_number < len(notes):
        notes[note_number] = note
        result = f'Note number {note_number} was changed'
    else:
        result = f'There is no note with number {note_number} in the notes'
    return result


# TODO 2 (Lara): check signature (`args` or `*args`? Just not sure...)
@input_error
def delete_note(notes, args):
    note_number = int(args[0])
    if note_number < len(notes):
        note_to_delete = notes[note_number]
        notes.pop(note_number)
        result = f'Note {str(note_to_delete)} was deleted'
    else:
        result = f'There is no note with number {note_number} in the notes'
    return result


# TODO 3 (Lara): change signature, see TODO 1
def new_tag(notes, *args):
    note_number = int(args[0][0])
    tag = args[0][1]
    if note_number < len(notes):
        notes.data[note_number].tags.append(tag)
        result = f'Tag {tag} was added to note {note_number}'
    else:
        result = f'There is no note with number {note_number}'
    return result


def sort_by_tag(notes, *args):
    res = '\tNotes sorted by tag:\n'
    number_of_notes = len(notes.data)
    if number_of_notes == 1:
        notes_sorted = notes
    if number_of_notes == 2:
        if notes.data[0] > notes.data[1]:
            notes.data[0], notes.data[1] = notes.data[1], notes.data[0]
    if number_of_notes >2:
        for i in range(len(notes.data) - 1):
            for j in range(len(notes.data) - 1 - i):
                if notes.data[j] > notes.data[j+1]:
                    notes.data[j], notes.data[j + 1] = notes.data[j+1], notes.data[j]
    return res + show_notes(notes)


def show_notes(notes, *args):
    res = ""
    for note in notes.data:
        res += '\t' + '{:<4}'.format(notes.data.index(note)) + str(note) + '\n'
    return res


def exit_notes(notes, *args):
    path = './database/notes_db.bin'
    with open(path, 'wb') as file:
        pickle.dump(notes, file)
    return f'Your notes saved in file {path}. Good bye!'


# TODO 4 (Lara): revise if this function is really needed
# Maybe it is better just to return in command_handle `None` value and docstring...
def help_notes(notes, *args):
    return args[0]


# TODO 5 (Lara): the same as TODO 4
def unknown(notes, *args):
    return args[0]


# COMMANDS = {
#     add_note: ("add",),
#     find_text: ("find",),
#     edit_note: ("edit",),
#     delete_note: ("delete",),
#     add_tag: ("add tag",),
#     sort_by_tag: ("sort by tag",),
#     exit_notes: ("exit",),
#     show_notes: ("show",),
# }
#
#
# def processing(customer_input):
#     for k in COMMANDS:
#         for command in COMMANDS[k]:
#             if customer_input.lower().strip().startswith(command):
#                 list_of_data = customer_input[len(command):].strip().split(" ")
#                 return k, list_of_data
#
#
# def main1():
#     path = 'database/notes_db.bin'
#     if os.path.isfile(path):
#         with open(path, 'rb') as file:
#             notes = pickle.load(file)
#     else:
#         notes = Notes()
#
#     while True:
#         customer_input = input(">>>")
#         func, data = processing(customer_input)
#         print(func(notes, data))
#         if func == exit:
#             break
#
#
# if __name__ == '__main__':
#
#     main1()
