import pickle

tasks = []
work_script = 1
status_task = 'Не выполнена'

def save():
    try:
        file = open("saves.bin", "wb")
        pickle.dump(tasks, file)
        file.close()
    except:
        print('Не удалось сохранить значение!')

def adding_task():
    while work_script == 1:
        task_name = input('Введите название задачи: ')
        task_description = input('Введите описание задачи: ')
        task = {
            "name": task_name.strip().replace(' ', '_'),
            "description": task_description.strip(),
            "status": status_task
        }
        tasks.append(task)
        save()
        print('Задача добавлена!')

        print("""
        1. Добавить еще задачу
        2. Вернутся в меню
        """)
        select_ = int(input('Введите номер нужного пункта: '))

        if select_ == 2:
            return


def list_tasks():
    for index in range(len(tasks)):
        print(f'{index}: Название: {tasks[index]["name"]} Описание: {tasks[index]["description"]} Статус: {tasks[index]["status"]}')

    return


def delete_task():
    for index in range(len(tasks)):
        print(f'{index}: Название: {tasks[index]["name"]} Описание: {tasks[index]["description"]} Статус: {tasks[index]["status"]}')

    del_num = int(input('Введите номер задачи которую надо удалить: '))
    del tasks[del_num]
    save()

    print("""
    1. Удалить еще одну задачу
    2. Назад
    """)

    select_ = int(input('Введите номер нужного пункта: '))

    if select_ == 1:
        delete_task()
    elif select_ == 2:
        return

def edit_task():
    for index in range(len(tasks)):
        print(f'{index}: Название: {tasks[index]["name"]} Описание: {tasks[index]["description"]} Статус: {tasks[index]["status"]}')

    select_ = int(input('Введите номер предложения: '))
    print("""
        1. Изменить название
        2. Изменить описание
        3. Вернутся назад
        """)
    sl_ = int(input('Номер пункта что хотите изменить: '))

    if sl_ == 1:
        edit_ = input('Новое название задачи: ')
        tasks[select_]['name'] = edit_
        save()
    elif sl_ == 2:
        edit_ = input('Новое описание задачи: ')
        tasks[select_]['description'] = edit_
        save()
    elif sl_ == 3:
        return

def completed_task():
    for index in range(len(tasks)):
        print(f'{index}: {tasks[index]}')

    select_ = int(input('Введите номер задачи: '))
    tasks[select_]['status'] = 'Выполнена'
    save()

def start_panel():
    while work_script == 1:
        print("""
        Функционал:

        1. Добавить задачу
        2. Список задач
        3. Редактирование задач
        4. Удалить задачу
        5. Отметить задачу как выполненную
        6. Выход""")

        select_variant = int(input('Введите номер нужного пункта: '))

        if select_variant == 1:
            adding_task()
        elif select_variant == 2:
            list_tasks()
        elif select_variant == 3:
            edit_task()
        elif select_variant == 4:
            delete_task()
        elif select_variant == 5:
            completed_task()
        elif select_variant == 6:
            return

file = open("saves.bin", "rb")
tasks = pickle.load(file)
file.close()

start_panel()