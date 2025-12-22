from typing import List
def squared_list(t: List[int]) -> List[int]:
    result = []
    for x in t:
        result.append(x * x)
    return result

nums = [1,2,3,4,5,6,7,8,9]
result = squared_list(nums)
result()