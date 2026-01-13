# LESSON 3/4
from collections import *
def group_a(words: list[str]) -> list[str]:
    anagrams = defaultdict(list)

    for word in words:
        count =[0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())

# words = ["eat", "tea", "ate", "pea", "ape"]
# print(group_a(words))


def k_freq_char(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

# nums = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5]
# print(k_freq_char(nums, 2))

import heapq

def heap_k_freq_char(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# print(heap_k_freq_char(nums,3))

def valid_p(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in  pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# s = ("()[]{}")
# print(valid_p(s))

def valid_p1(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

stack = Stack()

# stack.push(10)
# stack.push(20)
# stack.push(30)
#
# print(stack.size())
# stack.pop()
# print(stack.size())

class Stack2:
    def __init__(self):
        self.items = []

    def empty(self):
        len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[-1]
        return None


    def pop(self):
        if not self.empty():
            self.items.pop()
        return None

    def push(self, item):
        self.items.append(item)


# st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
#
# print(st.size())
# st.pop()
# print(st.size())


