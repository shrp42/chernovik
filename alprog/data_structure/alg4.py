# < 4. Стек / очередь >
# * Valid Parentheses: Проверка правильности скобок.

def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pairs.values():        # открывающая
            stack.append(char)
        else:                             # закрывающая
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


def test_is_valid():
    # ✅ Корректные скобки
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("{[()]}") == True
    assert is_valid("") == True  # пустая строка тоже корректна

    # ❌ Некорректные скобки
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("(") == False
    assert is_valid("]") == False

    print("Все тесты пройдены!")


# Запуск теста
test_is_valid()


# ----------------------------------------------------------------------


# * Реализация стека с методами push/pop/peek.
class Stack:
    """Класс для реализации стека (LIFO)"""

    def __init__(self):
        self.items = []

    # ------------------------
    # Вспомогательные методы
    # ------------------------
    def is_empty(self):
        """Проверка, пуст ли стек"""
        return len(self.items) == 0

    def size(self):
        """Вернуть количество элементов в стеке"""
        return len(self.items)

    def peek(self):
        """Посмотреть верхний элемент, не удаляя"""
        if not self.is_empty():
            return self.items[-1]
        return None

    # ------------------------
    # Основные методы
    # ------------------------
    def push(self, item):
        """Добавить элемент на верх стека"""
        self.items.append(item)

    def pop(self):
        """Удалить верхний элемент и вернуть его"""
        if not self.is_empty():
            return self.items.pop()
        return None



stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # 30
print(stack.pop())   # 30
print(stack.peek())  # 20

print(stack.size())  # 2
print(stack.is_empty())  # False

stack.pop()
stack.pop()
print(stack.is_empty())  # True


# ----------------------------------------------------------------------


# * Реализация очереди с приоритетом.
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        """
        Посмотреть элемент с наивысшим приоритетом
        без удаления
        """
        if self.heap:
            return self.heap[0][1]
        return None

    def push(self, item, priority):
        """
        Добавить элемент с приоритетом.
        В heapq по умолчанию минимальная куча,
        поэтому меньший приоритет выходит первым.
        """
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """
        Удалить элемент с наивысшим приоритетом
        (т.е. с наименьшим числом priority) и вернуть его
        """
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return item
        return None


pq = PriorityQueue()

pq.push("task1", priority=3)
pq.push("task2", priority=1)
pq.push("task3", priority=2)

print(pq.peek())  # task2 → наивысший приоритет
print(pq.pop())   # task2
print(pq.pop())   # task3
print(pq.pop())   # task1
print(pq.is_empty())  # True


# ----------------------------------------------------------------------


# * Sliding Window Problems: Максимум или сумма на окне длины k.

# Вариант суммы на окне длине К
def max_sum_window(nums, k):
    if not nums or k <= 0:
        return 0

    # начальная сумма первых k элементов
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        # сдвигаем окно на 1 вправо
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 3
print(max_sum_window(nums, k))  # 13 → окно [6,-1,4] или [4,1,8]


# Максимум на окне длины К
from collections import deque

def max_in_window(nums, k):
    if not nums or k <= 0:
        return []

    dq = deque()  # хранит индексы потенциальных максимумов
    result = []

    for i, num in enumerate(nums):
        # удаляем индексы, которые вышли из окна
        while dq and dq[0] <= i - k:
            dq.popleft()

        # удаляем все элементы меньше текущего, с конца deque
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # добавляем максимум текущего окна
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 3
print(max_in_window(nums, k))  # [3, 6, 6, 6, 4, 8, 8]