# < 3. Словари / хеш-таблицы >
# * Group Anagrams: Группировка слов-анаграмм.

# Вариант для коротких слов
from collections import defaultdict

def group_anagrams_sort(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


# Вариант для более длинных слов
from collections import defaultdict

def group_anagrams_count(words):
    anagrams = defaultdict(list)
    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        anagrams[tuple(count)].append(word)

    return list(anagrams.values())


# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams_sort(words)
# print("Результат для сортировки букв:", result)
# result2 = group_anagrams_count(words)
# print("Результат для подсчёта букв:", result2)


# ----------------------------------------------------------------------


# * Top K Frequent Elements: Найти k самых частых элементов.

# Решение через Counter
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)  # {'1':3, '2':2, '3':1} Считаем, сколько раз встречается каждое число
    return [num for num, freq in count.most_common(k)] # Сортируем элементы по частоте (от большей к меньшей)
                                                       # counter.most_common(k) возвращает список пар (число, частота)


# Альтернатива без сортировки — через heap (кучу)
from collections import Counter
import heapq

def top_k_frequent_heap(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get) # берём k элементов с самой большой частотой


# nums = [1,1,1,2,2,3,3,3,4,4,4,4]
# k = 3
#
# print(top_k_frequent(nums, k))       # через сортировку
# print(top_k_frequent_heap(nums, k))  # через кучу


# ----------------------------------------------------------------------


# * Valid Sudoku: Проверка корректности заполнения судоку.
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]      # множества для каждой строки
    cols = [set() for _ in range(9)]      # множества для каждого столбца
    boxes = [set() for _ in range(9)]     # множества для каждого 3x3 квадрата

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                continue  # пропускаем пустые клетки

            # проверка строки
            if num in rows[i]:
                return False
            rows[i].add(num)

            # проверка столбца
            if num in cols[j]:
                return False
            cols[j].add(num)

            # проверка квадрата 3x3
            box_index = (i // 3) * 3 + (j // 3)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)

    return True

board = [
  ["5","3",".",".","7",".","1",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

# print(is_valid_sudoku(board))  # True