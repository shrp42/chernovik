from typing import *
import time

# LESSON 1

def squared_list(t: List[int]) -> List[int]:
    result = []
    for x in t:
        result.append(x * x)
    return result

nums = [1,2,3,4,5,6,7,8,9]
result = squared_list(nums)



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
#LESSON 2
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

d_students(students)

def find_grade(students: Dict[str, float]) -> None:

    if not students:
        print('Dictionary is empty')
        return

    bottom_student = min(students.items(), key=lambda item:item[1])
    top_student = max(students.items(), key=lambda item:item[1])

    print(f"Student with the highest grade is {top_student[0]} with the grade {top_student[1]}")
    print(f"Student with the lowest grade is {bottom_student[0]} with the grade {bottom_student[1]}")

find_grade(students)