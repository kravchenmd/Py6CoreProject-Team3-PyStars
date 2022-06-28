from typing import Union

from console_bot.address_book import address_book_functions as f
from console_bot.address_book.address_book_class import AddressBook
from console_bot.notes.notes import Notes
from console_bot.sorting.sort import sort_folder
from console_bot.notes import notes as n


# TODO Finist docstring
def address_book_choose_command(cmd: list) -> tuple:
    """
    !!! In progress !!!
    Commands for AddressBook mode:
    - `close`, `exit`, `goodbye` - выход из программы
    - `hello` - выводит приветствие
    - `add` - добавление контакта в книгу. Количество аргументов может быть неполным. Например, 'add _name_' создаст контакт с пустыми полями номера телефона и даты рождения (при выводе заменяются '-'). Можно создать контакт только с именем и email, поставив 2 пробела после имени. Или же, например, с именем и датой рождения, поставив 3 пробела после имени (передавая пустые параметры для отсутствующих данных)
    - `change phone` - изменение номера контакта. Пример: 'change _name_ _old_phone_ _new_phone_'
    - `remove phone` - удаление телефона
    - `change email` - изменение email. Пример: 'change _name_ _old_email_ _new_email_'
    - `remove email` - удаление email
    - `phone` - показать номер контакта по имени
    - `email` - показать email по имени
    - `show all`/`show_all` - вывести все контакты с пагинацией (по умолчанию 2)
    - `edit birthday`/`edit_birthday` - изменить день рождения контакта
    - `days to birthday`/`days_to_birthday` - сколько дней до дня рождения контакта
    - `save`/`save_contacts` - сохранить контакты в файл, с использованием модуля `shelve`. По умолчанию сохранят в 'database/contacts.db'
    - `load` - загрузить контакты из файла, с использованием модуля `shelve`. По умолчанию загружается из 'database/contacts.db'
    - `find` - поиск контакта по имени или номеру телефона (ищет вхождения строки в этих полях)
    """

    match cmd:
        case ['close'] | ['exit'] | ['goodbye']:  # compare with one of the options in '[...]' ('|' is OR)
            return f.exit_program, []
        case ['hello']:
            return f.hello, cmd[1:]
        case ['add', 'contact', *args] | ['add_contact', *args]:  # *args is a list of all the arguments after 'add'
            return f.add_contact, args
        case ['remove', 'contact', *args] | ['remove_contact', *args]:
            return f.remove_contact, args
        case ['change', 'phone', *args] | ['change_phone', *args]:  # check 'change phone' or 'change_phone'
            return f.change_phone, args
        case ['remove', 'phone', *args] | ['remove_phone', *args]:
            return f.remove_phone, args
        case ['phones', *args] | ['show', 'phones', *args] | ['show_phones', *args]:
            return f.show_phone, args
        case ['show', 'all'] | ['show_all']:
            return f.show_all_phones, []
        case ['change', 'birthday', *args] | ['change_birthday', *args]:
            return f.change_birthday, args
        case ['remove', 'birthday', *args] | ['remove_birthday', *args]:
            return f.remove_birthday, args
        case ['days', 'to', 'birthday', *args] | ['days_to_birthday', *args]:
            return f.days_to_birthday, args
        case ['change', 'email', *args]:
            return f.edit_email, args
        case ['remove', 'email', *args]:
            return f.remove_email, args
        case ['birthday', 'in', *args] | ['birthday in', *args]:
            return f.birthday_in, args
        case ['save']:
            return f.save_contacts, cmd[1:]
        case ['load']:
            return f.load_contacts, cmd[1:]
        case ['find', 'contacts', *args] | ['find_contacts', *args]:
            return f.find_contacts, args
        case ['help']:
            return None, address_book_choose_command.__doc__
        case ['find', 'contact', *args] | ['find_contact', *args]:
            return f.find_contact, args
        case _:  # '_' corresponds to the case when no match is found
            return None, "Unknown command!"


# TODO Finist commands and docstring
def notes_choose_command(cmd: list) -> tuple:
    """
    Commands for Notes mode:
    - `add` - добавление новой заметки в Notes
    - `find` - поиск заметки по любому фрагменту (фрагмент заметки ввести через пробел) выводит все заметки, в которых найден указанный фрагмент
    - `edit` - редактирование заметки (формат команды - через пробел - номер заметки - новый текст и тег заметки)
    - `delete` - удаление заметки (необходимо внести порядковый номер заметки)
    - `show` - вывести все заметки в формате: номер тег текст
    - `new tag` - добавить тег к существующей заметке. Формат: номер заметки новый тег (с симоволом #)
    - `sort` - сортировать заметки по тегам
    - `exit` - выход из программы. Также, во время выхода Notes сохраняются в 'database/notes_db.bin'
    """

    match cmd:
        case['add', *args]:
            return n.add_note, args
        case ['find', *args]:
            return n.find_text, args
        case ['edit', *args]:
            return n.edit_note, args
        case ['delete', *args]:
            return n.delete_note, args
        case ['new', 'tag', *args]:
            return n.new_tag, args
        case ['sort', 'by', 'tag', *args]:
            return n.sort_by_tag, []
        case['exit', *args]:
            return n.exit_notes, []
        case['show', *args]:
            return n.show_notes, []
        case ['help']:
            return n.help_notes, notes_choose_command.__doc__
        case _:  # '_' corresponds to the case when no match is found
            return n.unknown, "Unknown command! For help type `help`"


# TODO Finist commands and docstring
def sorting_choose_command(cmd: list) -> tuple:
    """
    !!! In progress !!!
    Commands for sorting mode:
    - 'close', 'exit', 'goodbye' - exit the program
    - 'sort folder _path_', 'sort_folder _path_': sort the contacts by name
    """
    match cmd:
        case ['close'] | ['exit'] | ['goodbye']:
            return f.exit_program, []
        case ['help']:
            return None, sorting_choose_command.__doc__
        case ['sort', 'folder', *args] | ['sort_folder', *args]:
            return sort_folder, args
        case _:
            return None, "Unknown command!"


def handle_cmd(cmd: str, arg: Union[AddressBook, Notes, None], mode: str) -> tuple:
    cmd = cmd.strip().split(' ')

    match mode:
        case 'AddressBook':
            choose_command = address_book_choose_command
        case 'Sorting':
            choose_command = sorting_choose_command
        case "Notes":
            choose_command = notes_choose_command
        case _:
            return None, "ERROR: Unknown mode!"

    func, result = choose_command(cmd)
    if func and mode != 'Notes':
        args = [arg] + result if func not in (f.hello, f.exit_program) else result
        # else part to take into account hello() and show()
        result = func(*args)

    return func, result