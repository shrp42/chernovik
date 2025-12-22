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



def dict_students(d: dict[str, float]) -> None:
    for name,grade in d.items():
        print(f"{name}: {grade}")

students = {
    "John": 3.5,
    "Liza": 5.0,
    "Nick": 2.0,
    "Anna": 3.0,
    "Maga": 4.2
}

def find_grade(students: dict[str,float]) -> None:
    if not students:
        print("Dictionary is empty")
        return

    top_student = max(students.items(), key=lambda item: item[1])
    bottom_student = min(students.items(), key=lambda item: item[1])

    print(f"Student with the highest grade is {top_student[0]}: {top_student[1]}")
    print(f"Student with the lowest grade is {bottom_student[0]}: {bottom_student[1]}")


numbers = [1,2,3,4,3,2,4,6]
unique_numbers = set(numbers)
print(unique_numbers)




#<3. Работа со строками>
def count_vowels_consonants(text):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

    num_vowels = sum(1 for char in text if char in vowels)
    num_consonants = sum(1 for char in text if char in consonants)

    return num_vowels, num_consonants

text = "Привет, как дела?"
vowels_count, consonants_count = count_vowels_consonants(text)
print(f"Гласные: {vowels_count}, Согласные: {consonants_count}")



def is_palindrome(text):
    # Убираем пробелы и переводим все буквы в нижний регистр
    clean_text = ''.join(char.lower() for char in text if char.isalnum())

    # Сравниваем строку с её перевёрнутой версией
    return clean_text == clean_text[::-1]


text = "А роза упала на лапу Азора"
if is_palindrome(text):
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")



text = "Привет как дела"
words = text.split()
new_text = '-'.join(words)
print(new_text)