from typing import *
import time

#<LESSON 1>

# def squared_list(t: List[int]) -> List[int]:
#     result = []
#     for x in t:
#         result.append(x * x)
#     return result
#
# nums = [1,2,3,4,5,6,7,8,9]
# result = squared_list(nums)



def divided_by() -> List[int]:
    for x in range(1,100):
        if x % 5 == 0 and x % 2 == 0:
            print(x)


# def countdown(start: int = 10, end: int = 1, message: Optional[str] = "BOOM" * 100, delay = 0.5) -> None:
#     current = start
#     while current >= end:
#         print(current)
#         time.sleep(delay)
#         current -= 1
#     print(message)
#
# countdown()
#
#<LESSON 2>
#
def d_students(d: Dict[str, float]) -> None:

    if not d:
        print("Dictionary is empty")
        return

    for name,grade in d.items():
        print(f"{name}: {grade}")

students = {"Steven": 4.0,
     "Anna": 2.5,
     "Joshua": 3.2,
     "Peter":4.2}

# d_students(students)

def find_grade(students: Dict[str, float]) -> None:

    if not students:
        print('Dictionary is empty')
        return

    bottom_student = min(students.items(), key=lambda item:item[1])
    top_student = max(students.items(), key=lambda item:item[1])

    print(f"Student with the highest grade is {top_student[0]} with the grade {top_student[1]}")
    print(f"Student with the lowest grade is {bottom_student[0]} with the grade {bottom_student[1]}")

# find_grade(students)



#<LESSONS 1-2>
num = int(12)
# print(type(num))



def calculator(num1: float, num2: float, operation: str) -> float:
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль")
        return num1 / num2
    else:
        raise ValueError("Неизвестная операция")


def check(result):
    if result > 0:
        print(f"{result} положительное")
    elif result < 0:
        print(f"{result} отрицательное")
    else:
        print(f"{result} является нулем")


# try:
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     op = input("Операция (+ - * /): ")
#
#     result = calculator(a, b, op)
#     print("Результат:", result)
#     check(result)   # передаём результат в функцию
#
# except Exception as e:
#     print("Ошибка:", e)



def div():
    numbers = [n for n in range(1,150) if n % 6 == 0 and n % 7 == 0]

    if numbers:
        print(f'Эти числа делятся на ссссссикс сссевен {numbers}')
    else:
        print("Таких чисел нет")

# div()


def countdown(start: int = 10, end: int = 1, sms: str = "BOOM" * 10, delay = 0.4) -> None:
    current = start
    while current >= end:
        print(current)
        current -= 1
        time.sleep(delay)

    print(sms)

# countdown( )



def squared_list(l: List[int]) -> List[int]:
    result = []

    for x in l:
        result.append(x * x)
    return result

nums = [2,4,6,8,10]
result = squared_list(nums)
# print(result)



def dict_st(d: Dict[str,float]) -> None:
    for name,grade in d.items():
        print(f"{name}: {grade}")

students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68,
    "Ethan": 95,
    "Fiona": 77,
    "George": 83,
    "Hannah": 91,
    "Ivan": 64,
    "Julia": 88
}

# dict_st(students)

def find_gr(students: Dict[str, float]) -> None:
    if not students:
        print("Dictionary is empty !")
        return

    top_st = max(students.items(), key = lambda item : item[1])
    low_st = min(students.items(), key = lambda item : item[1])

    print(f"Student with the highest grade is {top_st[0]} with grade {top_st[1]}")
    print(f"Student with the lowest grade is {low_st[0]} with grade {low_st[1]}")

# find_gr(students)

#ПЕРЕЗАПИСАЛИ ФАЙЛ
nums = [9,8,7,6,5,4,3,2,1]

with open("file_nums.txt", "w") as file:
    for n in nums:
        file.write(str(n) + "\n")

#ПРОЧИТАЛИ И ВЫВЕЛИ
with open("file_nums.txt", "r") as file:
    nums_from_file = [int(n.strip()) for n in file]

print(nums_from_file)