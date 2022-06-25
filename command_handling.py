import functions as f
from classes import AddressBook


def choose_command(cmd: str) -> tuple:
    # redone with match-statement instead of if-ones
    # code is more readable and shorter! =)
    cmd = parse_command(cmd)

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
        case ['save']:
            return f.save_contacts, cmd[1:]
        case ['load']:
            return f.load_contacts, cmd[1:]
        case ['find', *args]:
            return f.find_contacts, args
        case _:  # '_' corresponds to the case when no match is found
            return None, "Unknown command!"


def parse_command(cmd: str) -> list:
    return cmd.strip().split(' ')  # apply strip() as well to exclude spaces at the ends


def handle_cmd(cmd: str, contacts: AddressBook) -> tuple:
    func, result = choose_command(cmd)
    if func:
        args = [contacts] + result if func not in (f.hello, f.exit_program) else result
        # else part to take into account hello() and show()
        result = func(*args)
    return func, result
