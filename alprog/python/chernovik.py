import random
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
# def d_students(d: Dict[str, float]) -> None:
#
#     if not d:
#         print("Dictionary is empty")
#         return
#
#     for name,grade in d.items():
#         print(f"{name}: {grade}")
#
# students = {"Steven": 4.0,
#      "Anna": 2.5,
#      "Joshua": 3.2,
#      "Peter":4.2}
#
# # d_students(students)
#
# def find_grade(students: Dict[str, float]) -> None:
#
#     if not students:
#         print('Dictionary is empty')
#         return
#
#     bottom_student = min(students.items(), key=lambda item:item[1])
#     top_student = max(students.items(), key=lambda item:item[1])
#
#     print(f"Student with the highest grade is {top_student[0]} with the grade {top_student[1]}")
#     print(f"Student with the lowest grade is {bottom_student[0]} with the grade {bottom_student[1]}")

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


#
# def dict_st(d: Dict[str,float]) -> None:
#     for name,grade in d.items():
#         print(f"{name}: {grade}")
#
# students = {
#     "Alice": 85,
#     "Bob": 72,
#     "Charlie": 90,
#     "Diana": 68,
#     "Ethan": 95,
#     "Fiona": 77,
#     "George": 83,
#     "Hannah": 91,
#     "Ivan": 64,
#     "Julia": 88
# }
#
# # dict_st(students)
#
# def find_gr(students: Dict[str, float]) -> None:
#     if not students:
#         print("Dictionary is empty !")
#         return
#
#     top_st = max(students.items(), key = lambda item : item[1])
#     low_st = min(students.items(), key = lambda item : item[1])
#
#     print(f"Student with the highest grade is {top_st[0]} with grade {top_st[1]}")
#     print(f"Student with the lowest grade is {low_st[0]} with grade {low_st[1]}")

# find_gr(students)

#ПЕРЕЗАПИСАЛИ ФАЙЛ
nums = [9,8,7,6,5,4,3,2,1]

with open("file_nums.txt", "w") as file:
    for n in nums:
        file.write(str(n) + "\n")

#ПРОЧИТАЛИ И ВЫВЕЛИ
with open("file_nums.txt", "r") as file:
    nums_from_file = [int(n.strip()) for n in file]

# print(nums_from_file)





# LESSON 1/2/3

# num = 12
# print(type(num))

def zer():
    while True:
        try:
            result = int(input("Enter the number: "))
            if result > 0:
                print(f"Number {result} bigger then 0")
            elif result < 0:
                print(f"Number {result} lower then 0")
            else:
                print("Your number is 0")
            break

        except ValueError:
            print("ENTER THE NUMBER!")
            continue

# zer()


def dv():
    nums = [n for n in range(1,500) if n % 5 == 0 and n % 103 == 0]

    if nums:
        print(f'These is numbers {nums}')
    else:
        print('There is no numbers')

# dv()



def count(start: int = 10, end: int = 1, m: str = "PIP", delay = 0.5) -> None:
    cur = start

    while cur >= end:
        print(cur)
        time.sleep(delay)
        cur -=1
    print(m)

# count()

def cv(p: list[int]) -> list[int]:
    return [z * z for z in p]

nms = [12, 10, 8, 6, 4, 2]
rs = cv(nms)
# print(rs)



def d_students(d: dict[str, float]) -> None:

    if not d:
        print("Dictionary is empty")
        return

    for name,grade in d.items():
        print(f"{name}: {grade}")

students = {
    "Mia": 9,
    "Alex": 7,
    "Lena": 10,
    "Igor": 6,
    "Sophia": 8
}

def mim_max(students: dict[str, float]) -> None:

    if not students:
        print("Dictionary is empty")
        return

    top_student = max(students.items(), key = lambda item:item[1])
    low_student = min(students.items(), key=lambda item: item[1])

    print(f"Student with the highest grade is {top_student[0]} with grade {top_student[1]}")
    print(f"Student with the lowest grade is {low_student[0]} with grade {low_student[1]}")

# mim_max(students)



# with open("file2_nums", "r") as file2:
#     l = [n.strip() for n in file2]
#     print(l)
#
# with open("file2_nums", "w") as file2:
#     nums = ("magic\n" * 10)
#
#     for n in nums:
#         file2.write(n)


class Worker:
    def __init__(self, name: str, salary: float):
        self.name = name
        self. salary = salary

    def __str__(self):
        return f"{self.name}: {self.salary}"

class Position(Worker):
    def __init__(self, name: str, salary: float, position: str):
        super().__init__(name,salary)
        self.position = position

    def __str__(self):
        return f"{self.name} position is {self.position} with salary {self.salary} per hour"

# worker1 = Position("John",250.00,"Chief")
# print(worker1)





# LESSON 1/2/3/4
# num = 2
# print(type(num))

def bol_men():
    while True:
        try:
            num = int(input("Enter your number:"))
            break
        except ValueError:
            print("Enter the number")

    if num < 0:
        print("Your number is less than 0")
    elif num > 0:
        print("Your number is greater than 0")
    else:
        print("Your number is 0")

# bol_men()


div = [n for n in range(1,100) if n % 3 == 0 and n % 5 == 0]
# print(div)


def counter(start: int = 10, end: int = 1, ms: str = "EsDeeKid", delay = 0.5) -> None:
    current = start

    while current >= end:
        print(current)
        time.sleep(delay)
        current -= 1
    print(ms)

# counter()


def square(l: List[int]) -> List[int]:
    return [x * x for x in l]

nums2 = [1,2,3,4,5,6,7,8,9]
nums = square(nums2)
# print(nums)


def d_workers(d: Dict[str, float]):

    if not d:
        print("Dictionary is empty !")

    for name,salary in d.items():
        print(f"{name}: {salary}")

workers = {"John": 200,
           "Liza": 95,
           "Kate": 110,
           "Bruce": 72}

def salaries(workers: Dict[str, float]) -> None:

    max_salary = max(workers.items(), key = lambda item: item[1])
    min_salary = min(workers.items(), key=lambda item: item[1])

    print(f"{max_salary[0]} has the highest salary {max_salary[1]} per hour")
    print(f"{min_salary[0]} has the lowest salary {min_salary[1]} per hour")

# salaries(workers)


# with open("file3_nums.txt", "w") as file3:
#     new_nums = [1,2,3,4,5,6,7,8,9]
#     for n in new_nums:
#         file3.write(f"{n}\n")
#
# with open("file3_nums.txt", "r") as file3:
#     file_nums = [int(n.strip()) for n in file3]
#     print(file_nums)


class Person:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"{self.name} is {self.gender}: {self.age} years old"

class Student(Person):
    def __init__(self,name: str, gender: str, age: int, grade: int):
        super().__init__(name,gender,age)
        self.grade = grade
    def __str__(self):
        return f"{self.name} is {self.gender}: {self.age} years old in {self.grade} grade"

# st1 = Student("Joseph","Male",17,11)
# print(st1)



def timing_decorator(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        print(f"\nFunction '{func.__name__}' has done in {end - start:.4f} seconds")
        return result
    return wrapper


# @timing_decorator
def fin():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a + b


for num in fin():
    if num > 100:
        break
    # print(num, end=" ")

# fin()



random_nums = [random.randint(1,100) for _ in range(12)]
sorted_list = sorted(random_nums)
# print(sorted_list)


sqr_list = [x*x for x in range(1,20)]
# print(sqr_list)

double = list(map(lambda x: x*2, sqr_list))
# print(f"List was doubled {double}")

filter = list(filter(lambda x: x % 4 == 0, double))
# print(f"List has only numbers that can be divided by 4 {filter}")