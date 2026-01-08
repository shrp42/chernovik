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