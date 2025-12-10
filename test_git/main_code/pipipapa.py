class Teacher:
      def __init__(self, name, subject):
          self.name = name
          self.subject = subject
 
      def teach(self):
          print(f"{self.name} is teaching {self.subject}.")

def main():
    teacher = Teacher("Mr. Smith", "Mathematics")
    teacher.teach()

print('sos')

print("sos" * 2)

print("чек ван чек ту проверяем тоси моси")

def main():
    sosbek = int(input("Сколько раз ? "))
    maga = f"Мага {sosbek} раз"
    print(maga)

if __name__ == "__main__":
    main()

def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operator = input("Введите оператор (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else:
                print("Неверный оператор.")
                continue

            print(f"Результат: {result}")
        except ValueError:
            print("Пожалуйста, введите действительные числа.")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль недопустимо.")

print("Калькулятор завершен.")
print("Проверка завершена успешно!")
print("Все работает как надо!")

calculator()
main()
pass