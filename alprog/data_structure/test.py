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

# nums = [-1,-2,4,53,-35,3]
# print(max_s(nums))



def two_sums(nums: list[int], target: int) -> int:
    seen = {}

    if not nums:
        return 0

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# nums = [1,2,2,2,3,4,4,4,55,43]
# print(two_sums(nums,8))



def rotate(nums: list[int], k: int) -> int:
    n = len(nums)

    if n == 0:
        return 0

    k = k % n

    def rever(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    rever(0, n - 1)
    rever(0, k - 1)
    rever(k, n - 1)

# nums = [1,2,3,4,5]
# k = rotate(nums, 2)
# print(nums)



def maximum(nums: list[int]) -> int:
    if not nums:
        return 0

    current_n = nums[0]
    max_n = nums[0]

    for j in (1, len(nums)):
        current_n = max(j, current_n + j)
        max_n = max(max_n, current_n)
    return max_n

# nums = [1,2,3,4,-5,2,3,4,2]
# k = maximum(nums)
# print(nums, k)



def rem_d(nums: list[int]) -> int:
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

# nums = [1,1,2,2,2,2,2,2,3,4,5,64,83,548,622,721]
# k = rem_d(nums)
# print(k, nums[:k])





# LESSON 2
def check_p1(s: str) -> bool:
    s = s.replace(" ","").lower()
    stuck = []

    for char in s:
        stuck.append(char)

    for char in s:
        if char != stuck.pop():
            return False

    return True



def check_p2(s: str) -> bool:
    s = s.replace(" ","").lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# print(check_p1("replace"))
# print(check_p2("репер"))





def check_a1(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)



def check_a2(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char,0) + 1

    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

# print(check_a2("sats","stasik"))



def check_l(s: str) -> int:
    s = s.replace(" ","").lower()
    char_set = set()
    left = 0
    maxl = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        maxl = max(maxl, right - left + 1)

    return maxl

print(check_l("qwertyui"))


def ch_a(s1: str, s2,str) -> bool:
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get[char, 0] + 1

    for char in s2:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True



def length(s: str) -> int:
    s = s.replace(" ","").lower()
    char_set = set()
    left = 0
    maxi = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        maxi = max(maxi, right - right + 1)

    return maxi