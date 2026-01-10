# < 2. Строки >
# * Проверка палиндрома.

# Вариант через стек (более медленный)
def check_p1(s: str) -> bool:
    s = s.replace(" ","").lower()
    stack = []

    for char in s:
        stack.append(char)

    for char in s:
        if char != stack.pop():
            return False
    return True


# Вариант через два указателя (более эффективный)
def check_p2(s: str) -> bool:
    s = s.replace(" ","").lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# print(check_p1("ре пЕр"))
# print(check_p2("ре пЕр"))
# print(check_p1("A man a plan a canal Panama"))
# print(check_p2("A man a plan a canal Panama"))


# ----------------------------------------------------------------------


# * Проверка анаграммы двух строк.

# Простой способ через сортировку (less effective)
def check_a1(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    return sorted(s1) == sorted(s2)


# Более эффективный способ через словарь (хэш-таблицу)
def check_a2(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
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

# print(check_a1("listen", "silent"))
# print(check_a2("listen", "silent"))
# print(check_a1("listen", "silents"))
# print(check_a2("listen", "silents"))


# ----------------------------------------------------------------------


# * Longest Substring Without Repeating Characters.
def check_length_dict(s: str) -> int:
    s = s.replace(" ", "").lower()
    char_dict = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_dict:
            left = max(left, char_dict[char] + 1)
        char_dict[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def test_check_length():
    # 1. Строка с уникальными символами
    assert check_length("abcdef") == 6, "Test 1 Failed"

    # 2. Строка с повторяющимися символами
    assert check_length("abcabcbb") == 3, "Test 2 Failed"

    # 3. Строка из одного символа
    assert check_length("aaaaa") == 1, "Test 3 Failed"

    # 4. Строка с несколькими подстроками без повторов
    assert check_length("pwwkew") == 3, "Test 4 Failed"

    # 5. Пустая строка
    assert check_length("") == 0, "Test 5 Failed"

    # 6. Строка с пробелами и спецсимволами
    assert check_length("a b c a b !") == 4, "Test 6 Failed"

    print("All tests passed!")

# Запуск тестов
# test_check_length()


# ----------------------------------------------------------------------


# * Longest Substring with At Most K Distinct Characters
def longest_sub_k(s: str, k: int):
    s = s.replace(" ","").lower()

    char_d = {}
    left = 0
    max_len = 0

    for right,char in enumerate(s):
            char_d[char] = char_d.get(char, 0) + 1
            while len(char_d) > k:
                left_char = s[left]
                char_d[left_char] -= 1
                if char_d[left_char] == 0:
                    del char_d[left_char]
                left += 1
            max_len = max(max_len, right - left + 1)

    return max_len

# longest_sub_k("eceba", 2)


# ----------------------------------------------------------------------


# * String Search (Boyer-Moore / KMP) — найти подстроку в строке.

# KMP с дата структурами
def compute_prefix(pattern: str) -> list[int]:
    """
    Строим префикс-функцию (π-массив) для KMP
    pi[i] = длина максимального префикса, который совпадает с суффиксом pattern[:i+1]
    """
    m = len(pattern)
    pi = [0] * m  # массив префикс-функции
    j = 0  # текущая длина совпадающего префикса
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]  # откат к предыдущему возможному совпадению
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Поиск всех вхождений pattern в text с помощью KMP
    """
    n, m = len(text), len(pattern)
    pi = compute_prefix(pattern)
    result = []
    j = 0  # индекс шаблона
    for i in range(n):  # проходим по тексту
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]  # откат по префикс-функции
        if text[i] == pattern[j]:
            j += 1
        if j == m:  # полное совпадение
            result.append(i - m + 1)
            j = pi[j - 1]  # продолжаем поиск
    return result



# Boyer-Moore с использованием словаря
def boyer_moore(text: str, pattern: str) -> list[int]:
    """
    Поиск всех вхождений pattern в text с помощью Boyer-Moore (bad character rule)
    """
    m, n = len(pattern), len(text)

    # Таблица последнего вхождения символов
    bad_char = {c: i for i, c in enumerate(pattern)}

    result = []
    s = 0  # сдвиг шаблона относительно текста
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:  # полное совпадение
            result.append(s)
            s += m  # сдвигаем на всю длину шаблона
        else:
            # сдвиг по правилу bad character
            s += max(1, j - bad_char.get(text[s + j], -1))
    return result


text = "ababcababc"
pattern = "ababc"
print("Boyer-Moore:", boyer_moore(text, pattern))  # [0, 5]
print("KMP:", kmp_search(text, pattern))  # [0, 5]