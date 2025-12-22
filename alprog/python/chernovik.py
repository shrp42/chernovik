from typing import *
import time
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
#
#
def