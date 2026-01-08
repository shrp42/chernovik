# LESSON 1
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([-3, 4, 3, 90], 0))
# print(two_sum([3, 3], 0))
# print(two_sum([3, 3], 6))
# print(two_sum([1,1,1,1,1,1,11,1,1], 6))


def remove_d(nums: list[int]) -> int:
    if not nums:
        return 0

    i = 0

    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1



def rotate(nums: list[int], k: int) -> int:
    n = len(nums)
    if n == 0:
        return

    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

# nums = [1,2,3,4,5,6,7,8,9]
# rotate(nums,4)
# print(nums)



def max_subarray(nums: list[int]) -> int:
    if not nums:
        return 0

    current_nums = nums[0]
    max_nums = nums[0]

    for num in nums[1:]:
        current_nums = max(num, current_nums + num)
        max_nums = max(max_nums, current_nums)

    return max_nums

# nums = [12,2,4,6,-100,14,13,-2,4,6,-7]
# print(max_subarray(nums))



def two_s(nums: list[int], target: int) -> int:
    if not nums:
        return 0

    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# nums = [1,2,3,4,5,6,7,8,9]
# print(two_s(nums,9))



def del_d(nums: list[int]) -> int:
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# nums = [1,1,2,42,42,42,52,52,52,654,343,21,12]
# k = del_d(nums)
# print(k, nums[:k])  # 2 [1,2]


def rot(nums: list[int], k: int) -> int:
    n = len(nums)
    if n == 0:
        return 0

    k = k % n

    def rev(left, right):
       while left < right:
           nums[left], nums[right] = nums[right], nums[left]
           left += 1
           right -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)

# nums = [10,20,30,40,50,60,70,80]
# rot(nums, 3)
# print(nums)


def max_s(nums: list[int]):
    if not nums:
        return 0

    cur_nums = nums[0]
    max_n = nums[0]

    for num in nums[1:]:
        cur_nums = max(num, cur_nums + num)
        max_n = max(max_n, cur_nums)

    return max_n

nums = [-1,-2,4,53,-35,3]
print(max_s(nums))