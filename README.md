# Py6Core: Project, Team 3 'PyStars'


<!-- Team -->

- :star: Michail Kravchenko (Team Leader)
- :star: Larysa Dmytrenko (Scrum Master)
- :star: Andrij Prytulskij (Presentation Manager)


<!-- Notes -->
- для правильного запуска через терминал PyCharm нужно запускать как пакет через команду: `py -m console_bot.main`в корневой папке проекта
  (См. https://stackoverflow.com/questions/50745094/modulenotfounderror-when-running-script-from-terminal)
- для избежания проблем со сторонними пакетами при установке с test.pypi нужно использовать команду: `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple console-bot-pystars`. С ключом `--extra-index-url` сторонние пакеты (подхватываются из параметра `install_requires' в файле `setup.py`) будут загружены установлены с pypi.org, а сам пакет - с test.pypi.org.


<!-- ABOUT THE PROJECT -->

Консольный бот имеет 3 режима для структурирования и хранения ваших данных.

Режимы:
1 - Address book
2 - Notes
3 - Sorting files

В каждом режиме команда "help" выводит список всех доступных команд.
Данные, введенные пользователем в каждом режиме, сохраняются в папке пользователя и доступны при следующем запуске.

## Список команд Address Book

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
- `days to borthday`/`days_to_borthday` - сколько дней до дня рождения контакта
- `save`/`save_contacts` - сохранить контакты в файл, с использованием модуля `shelve`. По умолчанию сохранят в 'database/contacts.db'
- `load` - загрузить контакты из файла, с использованием модуля `shelve`. По умолчанию загружается из 'database/contacts.db'
- `find` - поиск контакта по имени или номеру телефона (ищет вхождения строки в этих полях)

## Список команд Notes
- `add` - добавление новой заметки в Notes
- `find` - поиск заметки по любому фрагменту (фрагмент заметки ввести через пробел) выводит все заметки, в которых найден указанный фрагмент
- `edit` - редактирование заметки (формат команды - через пробел - номер заметки - новый текст и тег заметки)
- `delete` - удаление заметки (необходимо внести порядковый номер заметки)
- `show` - вывести все заметки в формате: номер тег текст
- `new tag`, `new_tag` - добавить тег к существующей заметке. Формат: номер заметки новый тег (с симоволом #)
- `sort by tag`, sort_by_tag - сортировать заметки по тегам
- `back` - вернуться в главное меню для выбора режима работы бота
- `exit` - выход из программы. Также, во время выхода Notes сохраняются в 'database/notes_db.bin'

## Список команд Sorting mode:
- `close`, `exit`, `goodbye` - exit the program
- `sort folder _path_`, `sort_folder _path_`: sort the contacts by name
- `back`: return to the main menu