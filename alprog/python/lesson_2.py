from typing import Optional
from typing import List
from typing import Tuple

# def hello():
#     print("Hello world")



##<1. Функции>
# def is_prime(n: int) -> bool:
#
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#
#     return True
#
# num = int(input("Enter your number:"))
# if is_prime(num):
#     print(f"Number {num} is prime")
# else:
#     print(f"Number {num} is not prime")



# def square_nums(numbers: list[int,...]) -> None:
#     result = []
#     for n in numbers:
#         result.append(n * n)
#     return result
#
# print(square_nums([1,2,3,4,5,6,7,8,9]))



# def dict_students(d: dict[str, float]) -> None:
#     for name,grade in d.items():
#         print(f"{name}: {grade}")
#
# students = {
#     "John": 3.5,
#     "Liza": 5.0,
#     "Nick": 2.0,
#     "Anna": 3.0,
#     "Maga": 4.2
# }
#
# def find_grade(students: dict[str,float]) -> None:
#     if not students:
#         print("Dictionary is empty")
#         return
#
#     top_student = max(students.items(), key=lambda item: item[1])
#     bottom_student = min(students.items(), key=lambda item: item[1])
#
#     print(f"Student with the highest grade is {top_student[0]}: {top_student[1]}")
#     print(f"Student with the lowest grade is {bottom_student[0]}: {bottom_student[1]}")


# numbers = [1,2,3,4,3,2,4,6]
# unique_numbers = set(numbers)
# print(unique_numbers)




#<3. Работа со строками>
