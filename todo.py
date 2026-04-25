import datetime
from os import makedirs, listdir, path, remove


folder = "todo"

help = '''Помощь (как просили)

Работа с командами заключается в вводе по одной команде.
Для указания задачи пишите название а не номера в списке.

help, ?, h - Помощь. (Ты это ввел, зачем ты это читаешь???)
create, c - Создать задачу. Можно редактировать если указать уже существующюю задачу.
delete, d - Удалить задачу.
confirm, conf - Указать задачу как выполненную.
unconfirm, uconf - Указать задачу как не выполненную.
list, l - Посмотреть задачи.
show, s - Просмотреть задачу.
exit, e - Выйти из программы.
'''

makedirs("todo", exist_ok=True)

print("Введите комманду. ? - для просмотра комманд")

def list():
    for i, file in enumerate(listdir(folder), start=1):
                name, _ = path.splitext(file)
                print(f"{i}) {name}")

def create():
    name = input("Введите краткое название задачи -$ ")
    print("Готово!")
    desc = input("Введите описание -$ ")
    print("Готово!")

    with open(f"{folder}/{name}.txt", "w", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime("%d.%m.%Y - %H:%M")}\n{desc}\nнет")

def delete():
    list()
    name = input("Введите название задачи которую хотите удалить -$ ")
    try:
        remove(f"{folder}/{name}.txt")

    except FileNotFoundError: print(f"Файл не найден!")


def confirm():
    list()
    
    name = input("Введите название задачи которую хотите отметить -$ ")

    try:
        with open(f"{folder}/{name}.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) >= 3:
            lines[2] = "да"

        with open(f"{folder}/{name}.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)

        print("Готово!")
            
    except FileNotFoundError: print(f"Файл не найден!")

def unconfirm():
    list()
    
    name = input("Введите название задачи которую хотите отметить -$ ")

    try:
        with open(f"{folder}/{name}.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) >= 3:
            lines[2] = "нет"

        with open(f"{folder}/{name}.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)

        print("Готово!")
    
    except FileNotFoundError: print(f"Файл не найден!")

def show():
    list()

    name = input("Введите название задачи которую хотите просмотреть -$ ")

    try:
        with open(f"{folder}/{name}.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Задача {name}:\n {lines[1]}\n Выполненно: {lines[2]}\n Созданно: {lines[0]}")

    except FileNotFoundError: print(f"Файл не найден!")


while True:
    inp = input("-$ ")

    match inp:
        case "?": print(help)
        case "h": print(help)
        case "help": print(help)


        case "c": create()
        case "create": create()
        
        case "d": delete()
        case "delete": delete()
        
        case "conf": confirm()
        case "confirm": confirm()
        
        case "uconf": unconfirm()
        case "unconfirm": unconfirm()

        case "l": list()
        case "list": list()

        case "s": show()
        case "show": show()

        case "e": break
        case "exit": break

        case default: print("Не найденно")

print("Выход...")
