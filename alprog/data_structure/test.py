#Линейный алгоритм - подходит для маленьких баз данных

# def locate_card(cards,number):
#     position = 0
#
#     while position < len(cards):
#         if cards[position] == number:
#             return position
#         position += 1
#
#     return -1
#
# cards = [1,2,3,4,5,6,7,8,9]
# number = 6
# result = locate_card(cards,number)
# if result != -1:
#     print(f"Card position is = {result + 1}")
# else:
#     print("Card not founded")
#
# print('---Testing---')
#
# tests = [
#     {'input': {'cards': [2,3,3,4,4,4,42,52], 'number': 42}, 'output': 6},
#     {'input': {'cards': [], 'number': 3}, 'output': -1},
#     {'input': {'cards': [1,2,3,4,5,6], 'number': 9}, 'output': -1}
# ]
# for i, test in enumerate(tests):
#     result = locate_card(**test['input'])
#     if result == test['output']:
#         print(f'Test {i} passed')
#     else:
#         print(f"test {i} falied")
#
#
# # --------------------------------------------------------------------------------------
#
#
# # Бинарный поиск - подходит для работы с большими базами данных
# #
# def test_location(cards,query,mid):
#     if cards[mid] == query:
#         if mid-1 >= 0 and cards[mid-1] == query:
#             return "Left"
#         else:
#             return "Founded"
#     elif cards[mid] < query:
#         return "Left"
#     else:
#         return "Right"
#
# def locate_card(cards,query):
#     lo, hi = 0, len(cards)-1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(cards,query,mid)
#         if result == "Founded":
#             return mid
#         elif result == "Left":
#             hi = mid - 1
#         elif result == "Right":
#             lo = mid + 1
#     return -1
#
# cards = [10,9,8,7,6,5,4,3,2,1]
# query = 2
# locate_card(cards,query)
# result = locate_card(cards, query)
# print(f"Card found at position: {result}")
#
# # --------------------------------------------------------------------------------------
#
# def locate_card(cards,query):
#     lo, hi = 0, len(cards) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(cards,query,mid)
#         if result == "founded":
#             return mid
#         elif result == "left":
#             hi = mid - 1
#         elif result == 'right':
#             lo = mid + 1
#     return -1
#
# def test_location(cards,query,mid):
#     if cards[mid] == query:
#         if mid-1 >= 0 and cards[mid-1] == query:
#             return "left"
#         else:
#             return "founded"
#     elif cards[mid] < query:
#         return "left"
#     else:
#         return "right"
#
# cards = [6,5,4,3,2,1]
# query = 1
# result = locate_card(cards,query)
# print(f"Positon of card is {result}")
#
# # --------------------------------------------------------------------------------------
#
# def locate_card(cards,number):
#     lo, hi = 0, len(cards) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(cards,number,mid)
#         if result == 'founded':
#             return mid
#         elif result == 'left':
#             hi = mid - 1
#         elif result == 'right':
#             lo = mid + 1
#     return -1
#
# def test_location(cards,number,mid):
#     if cards[mid] == number:
#         if mid-1 >= 0 and cards[mid-1] == number:
#             return 'left'
#         else:
#             return 'founded'
#     elif cards[mid] < number:
#         return 'right'
#     else:
#         return 'left'
#
# cards = list(range(1,101))
# number = 17
# result = locate_card(cards,number)
#
# if result == -1:
#     print(f'Number {number} not founded')
# else:
#     print(f'Number {number} was founded at position {result}')
#
#
# def locate_card(cards,query):
#     lo,hi = 0, len(cards) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(cards,query,mid)
#         if result == "left":
#             hi = mid - 1
#         elif result == "right":
#             lo = mid + 1
#         elif result == "founded":
#             return mid
#     return -1
#
# def test_location(cards,query,mid):
#     if cards[mid] == query:
#         if mid-1 >= 0 and cards[mid-1] == query:
#             return "left"
#         else:
#             return "founded"
#     elif cards[mid] < query:
#         return "right"
#     else:
#         return "left"
#
#
# cards = list(range(1,100000))
# query = 78939
# result = locate_card(cards,query)
# if result == -1:
#     print(f'Number {query} not founded')
# else:
#     print(f'Number {query} was founded at position {result + 1}')


# --------------------------------------------------------------------------------------

