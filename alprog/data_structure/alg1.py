# <1. Массивы и списки>
# * Two Sum: Найти два числа в массиве, сумма которых равна заданному числу.
def two_sum(nums, target):
    seen = {}  # словарь: число -> индекс

    for p, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], p]
        seen[num] = p

# Тесты
# print(two_sum([2, 7, 11, 15], 9))        # [0, 1]
# print(two_sum([-3, 4, 3, 90], 0))       # [0, 2]
# print(two_sum([3, 3], 6))               # [0, 1]




# * Remove Duplicates from Sorted Array: Удалить дубликаты in-place.
def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # индекс последнего уникального элемента

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

# nums = [1,1,2]
# k = remove_duplicates(nums)
# print(k, nums[:k])  # 2 [1,2]
#
# nums = [0,0,1,1,1,2,2,3,3,4]
# k = remove_duplicates(nums)
# print(k, nums[:k])  # 5 [0,1,2,3,4]
#
# nums = []
# k = remove_duplicates(nums)
# print(k, nums[:k])
#
# nums = [1]
# k = remove_duplicates(nums)
# print(k, nums[:k])




# * Rotate Array: Повернуть массив на k позиций.
def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return

    k = k % n  # если k больше длины массива

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)       # шаг 1
    reverse(0, k - 1)       # шаг 2
    reverse(k, n - 1)       # шаг 3

# nums = [1,2,3,4,5,6,7] 2,3,4,5,6,7,1
# rotate(nums, 9)
# print(nums)  # [5,6,7,1,2,3,4]




# * Maximum Subarray (Kadane’s algorithm): Найти под_массив с максимальной суммой.
def max_subarray(nums):
    if not nums:
        return 0

    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray(nums))  # 6
