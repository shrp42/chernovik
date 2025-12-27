#<1. Проект «Калькулятор»>
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def calculator():
    while True:
        print("\nВведите команду: сложение (+), вычитание (-), умножение (*), деление (/), выход (exit)")
        command = input("Команда: ").strip().lower()

        if command == "выход" or command == "exit":
            print("Выход из калькулятора...")
            break

        if command in ("+", "-", "*", "/"):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите число!")
                continue

            if command == "+":
                print(f"Результат: {add(num1, num2)}")
            elif command == "-":
                print(f"Результат: {subtract(num1, num2)}")
            elif command == "*":
                print(f"Результат: {multiply(num1, num2)}")
            elif command == "/":
                print(f"Результат: {divide(num1, num2)}")
        else:
            print("Неизвестная команда, попробуйте снова.")

# Запуск калькулятора
calculator()
