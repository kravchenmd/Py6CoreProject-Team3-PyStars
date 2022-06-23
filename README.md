# Py6Core: Project, Team 3 'PyStars'

<!-- Team -->

- :star: Michail Kravchenko (Team Leader)
- :star: Larysa Dmytrenko (Scrum Master)
- :star: Andrij Prytulskij (Developper, Presentation Manager)

<!-- ABOUT THE PROJECT -->

## Список команд

- `close`, `exit`, `goodbye` - выход из программы
- `hello` - выводит приветствие
- `add` - добавление контакта в книгу. Количество аргументов может быть неполным. Например, 'add _name_' создаст контакт с пустыми полями номера телефона и даты рождения (при выводе заменяются '-'). Можно создать контакт только с именем и датой рождения, поставит 2 пробела после имени (передав пустой параметр для номера)
- `change` - изменение номера контакта. Пример: 'change _name_ _phone_'
- `remove` - удаление контакта
- `phone` - показать номер контакта по имени
- `show all`/`show_all` - вывести все контакты с пагинацией (по умолчанию 2)
- `edit birthday`/`edit_birthday` - изменить день рождения контакта
- `days to borthday`/`days_to_borthday` - сколько дней до дня рождения контакта
- `save`/`save_contacts` - сохранить контакты в файл, с использованием модуля `shelve`. По умолчанию сохранят в 'database/contacts.db'
- `load` - загрузить контакты из файла, с использованием модуля `shelve`. По умолчанию загружается из 'database/contacts.db'
- `find` - поиск контакта по имени или номеру телефона (ищет вхождения строки в этих полях)
