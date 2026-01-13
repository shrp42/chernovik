# LESSON 1
from heapq import nlargest


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

# print(check_l("qwertyui"))


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




# LESSON 1/2
def two_ss(nums: list[int], target: int) -> list[int]:
    if not nums:
        print("List is empty")
        return None

    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


def del_d(nums: list[int]) -> list[int]:
    if not nums:
        return []

    i = 0

    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return nums[:i + 1]

# print(del_d([1,1,1,1,1,2,3,4,5,6,7,8,9]))


def pov(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []

    n = len(nums)

    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return nums

# nums = [1,2,3,4,5,6,7,8]
# print(pov(nums, 4))


def max_sub(nums: list[int]) -> int:
    if not nums:
        return 0

    current_nums = max_nums = nums[0]

    for num in nums[1:]:
        current_nums = max(num, current_nums + num)
        max_nums = max(max_nums, current_nums)

    return max_nums

# print(max_sub([1, -2, 3, 4, -1, 2, 1, -5, 4]))
# print(max_sub([-3, -1, -2]))


def check_p(s: str) -> bool:
    s = s.replace(" ","").lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# print(check_p("A man a plan a canal Panama"))


def check_a(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False

    return True

# print(check_a("kakashik", "kakashki"))
# print(check_a("kakashik", "kakashk"))
# print(check_a("kakashik", "kakashka"))
# print(check_a("", ""))


def check_l(s: str) -> int:
    s = s.replace(" ", "").lower()

    char_d = {}
    left = 0
    max_l = 0

    for right, char in enumerate(s):
        if char in char_d:
            left = max(left, char_d[char] + 1)
        char_d[char] = right
        max_l = max(max_l, right - left + 1)

    return max_l



def longest_sub_k(s: str, k: int) -> int:
    s = s.replace(" ", "").lower()

    char_d = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_d[char] = char_d.get(char, 0) + 1
        while len(char_d) > k:
            left_char = s[left]
            char_d[left_char] -= 1
            if char_d[left_char] == 0:
                del char_d[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

# print(longest_sub_k("gdhjagshdgajhsg", 6))


def check_a2(s:str) -> int:
    s = s.replace(" ", "").lower()

    char_d = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_d:
            left = max(left, char_d[char] + 1)
        char_d[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

def check_lsk(s: str, k: int) -> int:
    s = s.replace(" ", "").lower()

    char_dict = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_dict[char] = char_dict.get(char, 0) + 1
        while len(char_dict) > k:
            char_left = s[left]
            char_dict[char_left] -= 1
            if char_dict[char_left] == 0:
                del char_dict[char_left]
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len


# LESSON 1-2:

def  check_p(s: str) -> bool:
    s = s.replace(" ","").lower()

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def check(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[cahr] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


def check_longest_sub(s: str) -> int:
    s = s.replace(" ", "").lower()

    char_d = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_d:
            left = max(left, char_d[char] + 1)
        char_d[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def check_longest_sub_k(s: str, k: int) -> int:
    s = s.replace(" ", "").lower()

    char_d = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_d[char] = char_d.get(char, 0) + 1
        while len(char_d) > k:
            left_char = s[left]
            char_d[left_char] -= 1
            if char_d[left_char] == 0:
                del char_d[left_char]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len

# print(check_longest_sub_k("aaaabcddddddddekhjkh", 4))


# LESSON 1/2/3


def p_check(s: str) -> bool:
    s = s.replace(" ","").lower()

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def a_check(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


def long_sub(s: str) -> int:
    s = s.replace(" ", "").lower()

    char_d = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_d:
            left = max(left, char_d[char] + 1)
        char_d[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def long_sub_k(s: str, k: int) -> int:
    s = s.replace(" ", "").lower()

    char_dictionary = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        char_dictionary[char] = char_dictionary.get(char, 0) + 1
        while len(char_dictionary) > k:
            char_left = s[left]
            char_dictionary[char_left] -= 1
            if char_dictionary[char_left] == 0:
                del char_dictionary[char_left]
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length


from collections import *

def count_ann(words: list[str]) -> list[str]:
    anagrams = defaultdict(list)

    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(count_ann(words))


def most_n(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

# nums = [1,1,1,1,11,2,1,1,1,1,11,11,11,2,2,3,4,455,5,5,55,57,7]
# print(most_n(nums, 3))

import heapq

def most_n_heap(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# nums = [1,1,1,1,11,2,1,1,1,1,11,11,11,2,2,3,4,455,5,5,55,57,7]
# print(most_n_heap(nums, 3))



def group_a(words: list[str]) -> list[str]:
    anagrams = defaultdict(list)

    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_a(words))


def most_n(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

def most_n_heap(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


# nums = []
# print(most_n(nums,2))
# print(most_n_heap(nums,2))


