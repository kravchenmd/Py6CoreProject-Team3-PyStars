import os
import sys
from typing import Union

if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in sys.path:
    from address_book import address_book_functions as f
    from address_book.address_book_class import AddressBook
    from notes.notes import Notes
    from sorting.sort import sort_folder
    from notes import notes as n
else:
    from .address_book import address_book_functions as f
    from .address_book.address_book_class import AddressBook
    from .notes.notes import Notes
    from .sorting.sort import sort_folder
    from .notes import notes as n


def address_book_choose_command(cmd: list) -> tuple:
    """
    Commands for AddressBook mode:
    - `close`, `exit`, `goodbye` - выход из программы
    - `hello` - выводит приветствие
    - 'back' - return to the main menu
    - `add contact`, `add_contact` - добавление контакта в книгу
    - `remove contact`, `remove_contact` - удаление контакта из книги
    - `change phone`, `change_phone` - изменение номера контакта
    - `remove phone`, `remove_phone` - удаление телефона
    - `show email`, `show_email` - показать email по имени
    - `change email`, `change_email` - изменение email. Пример: 'change _name_ _old_email_ _new_email_'
    - `remove email`, `remove_email` - удаление email
    - `phones`, `show phones`, `show_phones` - показать номера контакта по имени
    - `show all`, `show_all` - вывести все контакты с пагинацией (по умолчанию 2)
    - `edit birthday`, `edit_birthday` - изменить день рождения контакта
    - `days to birthday`, `days_to_birthday` - сколько дней до дня рождения контакта
    - 'birthday in', `birthday_in` - вывести список контактов, у которых ДР через заданное кол-во дней
    - `save`, `save_contacts` - сохранить контакты в файл, с использованием модуля `shelve`.
    - `load` - загрузить контакты из файла, с использованием модуля `shelve`.
    - `find contact`, `find_contact` - поиск контакта по имени или номеру телефона (ищет вхождения строки в этих полях)
    """

    match cmd:
        case ['close'] | ['exit'] | ['goodbye']:  # compare with one of the options in '[...]' ('|' is OR)
            return f.exit_program, []
        case ['hello']:
            return f.hello, cmd[1:]
        case ['back']:
            return f.back, []
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
        case ['change', 'email', *args] | ['change_email', *args]:
            return f.edit_email, args
        case ['remove', 'email', *args]:
            return f.remove_email, args
        case ['show', 'email', *args] | ['show_email', *args]:
            return f.show_email, args
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


def notes_choose_command(cmd: list) -> tuple:
    """
    Commands for Notes mode:
    - `add` - добавление новой заметки в Notes
    - `find` - поиск заметки по любому фрагменту (фрагмент заметки ввести через пробел) выводит все заметки, в которых найден указанный фрагмент
    - `edit` - редактирование заметки (формат команды - через пробел - номер заметки - новый текст и тег заметки)
    - `delete` - удаление заметки (необходимо внести порядковый номер заметки)
    - `show` - вывести все заметки в формате: номер тег текст
    - `new tag`, `new_tag` - добавить тег к существующей заметке. Формат: номер заметки новый тег (с симоволом #)
    - `sort by tag`, sort_by_tag - сортировать заметки по тегам
    - 'back' - return to the main menu, повернутися в головне меню
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
        case ['new', 'tag', *args] | ['new_tag', *args]:
            return n.new_tag, args
        case ['sort', 'by', 'tag', *args] | ['sort_by_tag', *args]:
            return n.sort_by_tag, []
        case['exit', *args]:
            return n.exit_notes, []
        case['show', *args]:
            return n.show_notes, []
        case ['back']:
            return f.back, []
        case ['help']:
            return n.help_notes, notes_choose_command.__doc__
        case _:  # '_' corresponds to the case when no match is found
            return n.unknown, "Unknown command! For help type `help`"


def sorting_choose_command(cmd: list) -> tuple:
    """
    Commands for sorting mode:
    - 'close', 'exit', 'goodbye' - exit the program
    - 'sort folder _path_', 'sort_folder _path_': sort the contacts by name
    - 'back': return to the main menu
    """
    match cmd:
        case ['close'] | ['exit'] | ['goodbye']:
            return f.exit_program, []
        case ['help']:
            return None, sorting_choose_command.__doc__
        case ['back']:
            return f.back, []
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

    if mode != 'Notes' and func is not None:
        if mode == 'AddressBook':
            args = [arg] + result if func not in (f.hello, f.exit_program, f.back) else result
        else:  # for Sorting mode
            args = result
        result = func(*args)

    return func, result
