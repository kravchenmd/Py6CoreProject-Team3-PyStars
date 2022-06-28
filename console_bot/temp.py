# from prompt_toolkit import prompt
# from prompt_toolkit.completion import WordCompleter
# import psutil
#
# import os
# # psutil.Process(os.getpid()).parent.name
# print(psutil.Process(os.getppid()).parent)
# parent_names = {parent.name() for parent in psutil.Process().parents()}
# print(set(parent_names))
#
#
# # html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
# # text = prompt('Enter HTML: ', completer=html_completer)
# # print('You said: %s' % text)

import getpass

password = getpass.getpass("Entering password: ")

print(password)