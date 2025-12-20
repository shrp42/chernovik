from typing import Optional
import time
from typing import List
from typing import Tuple
#

# <БАЗА>
def hello ():
    print("Hello World")




# <1. Переменные и типы данных>
def bunch_of_smt():

    word = str("word")
    num = int(12)
    float_num = float(4.2)
    bool_smt = True
    print(word,num,float_num,bool_smt)




# <2. Операции и выражения>
def sum_nums():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = input("Enter what you want to do: ")
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print(a / b)
    elif c == "%":
        print(a % b)
    elif c == "**":
        print(a ** b)
    else:
        print("Unknown operation")




#<3. Условные конструкции>
def classify_num(num: int) -> str:
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    return "Your number is zero"

def classify_num_main():
    try:
        num = int(input("Enter your number: "))
    except ValueError:
        print("Enter valid number")
        return

    result = classify_num(num)
    print(f"Your {num} is {result}")



def leap_or_no(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def leap_or_no_main():
    try:
        year = int(input("Enter your year: "))
    except ValueError:
        print("Print valid year")
        return

    if leap_or_no(year):
     print(f"Year {year} is leap")
    else:
     print(f"Year {year} is not leap")





#<4. Циклы>
def divide_by_3_5():
    for num in range(1,100):
        if num % 3 == 0 and num % 5 == 0:
            print(num)


def countdown(start: int = 10, end: int = 0, message: Optional[str] = "BOOM", delay: float = 0.3) -> None:

    current = start
    while current >= end:
        print(current)
        time.sleep(delay)
        current -= 1
    print(message)



#
#<5. Списки и кортежи>
def anal_nums(nums: List[int]) -> None:

    if not nums:
        print("Thr list is empty")
        return

    total = sum(nums)
    maximum = max(nums)
    minimum = min(nums)
    average = total / len(nums)

    print(f"Numbers: {sorted(nums)} \n",
          f"Total {total}\n",
          f"Maximum {maximum}\n",
          f"Minimum {minimum}\n",
          f"Average {average}\n")

def anal_nums_main():
    nums = [1,23,56,54,89,45,27]
    anal_nums(nums)




def reverse_nums() -> None:
    nums = [9,8,7,6,5,4,3,2,1]
    nums.reverse()
    print(nums)


def reversed_nums() -> None:
    numbers = [1,2,3,4,5,6,7,8,9]
    print(numbers[::-1])


def demo_tuple(t: Tuple[int,...]) -> None:

    print("Original tuple", t)
    try:
        t[0] = 900
    except TypeError as e:
        print("Tuple cannot be modified",e)

my_tuple: Tuple[int,...] = (1,2,3,4,5,6,7,8,9)



if __name__ == "__main__":
    hello()
