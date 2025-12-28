#< 1. Проект «Калькулятор»>
def add(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("Can't divide by 0")
        return None
    return a / b

def calculator():
    while True:
        print("\nEnter command: add (+), minus (-), multiply (*), divide (/), exit (exit)")
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Exit calculator...")
            break

        if command in ("+","-","/","*"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Enter valid number !")
                continue

            if command == "+":
                print(f"Result: {add(num1,num2)}")
            if command == "-":
                print(f"Result: {minus(num1,num2)}")
            if command == "*":
                print(f"Result: {multiply(num1,num2)}")
            if command == "/":
                result = divide(num1, num2)
                if result is not None:
                    print(f"Result: {result}")
        else:
            print("Unknown command !")

# calculator()





# < 2. Проект «Текстовый анализ» >
from collections import Counter

def analyze_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()

    symbols = ".,!?;:-()\"'"
    for s in symbols:
        text = text.replace(s, "")

    words = text.split()
    counter = Counter(words)

    print(f"Общее количество слов: {len(words)}")
    print(f"Уникальных слов: {len(counter)}")
    print("\nЧастота слов:")

    for word, count in counter.items():
        print(f"{word}: {count}")

# вызов функции
analyze_text("file_text.txt")





# < 3. Проект «Игра Угадай число» >
import random

def guess_number():
    # Загадали число от 1 до 100
    number = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Пожалуйста, вводите только числа!")
            continue

        if guess < number:
            print("Больше!")
        elif guess > number:
            print("Меньше!")
        else:
            print(f"Поздравляю! Вы угадали число {number}!")
            break

# Запуск игры
guess_number()










# < 4. Проект «Менеджер задач»>
import json

FILENAME = "tasks.json"

# Загрузка задач из файла
def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)  # возвращаем словарь с задачами
    except FileNotFoundError:
        return {}  # если файла нет, возвращаем пустой словарь

# Сохранение задач в файл
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

# Добавление задачи
def add_task(tasks):
    task_id = input("Введите уникальный ID задачи: ")
    if task_id in tasks:
        print("Задача с таким ID уже существует!")
        return
    description = input("Введите описание задачи: ")
    tasks[task_id] = description
    save_tasks(tasks)
    print("Задача добавлена!")

# Удаление задачи
def delete_task(tasks):
    task_id = input("Введите ID задачи для удаления: ")
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print("Задача удалена!")
    else:
        print("Задача с таким ID не найдена!")

# Показать все задачи
def show_tasks(tasks):
    if not tasks:
        print("Задач пока нет.")
        return
    print("\nСписок задач:")
    for task_id, description in tasks.items():
        print(f"{task_id}: {description}")

# Главная функция
def task_manager():
    tasks = load_tasks()

    while True:
        print("\nВыберите действие: add, delete, show, exit")
        command = input("Введите команду: ").strip().lower()

        if command == "exit":
            print("Выход из менеджера задач...")
            break
        elif command == "add":
            add_task(tasks)
        elif command == "delete":
            delete_task(tasks)
        elif command == "show":
            show_tasks(tasks)
        else:
            print("Неизвестная команда!")

# Запуск программы
task_manager()
