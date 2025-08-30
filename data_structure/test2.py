# Бинарный поиск - подходит для работы с большими базами данных

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

# cards = [10,9,8,7,6,5,4,3,2,1]
# query = 2
# locate_card(cards,query)  
# result = locate_card(cards, query)
# print(f"Card found at position: {result}")

# --------------------------------------------------

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
    
# cards = [6,5,4,3,2,1]
# query = 1
# result = locate_card(cards,query)
# print(f"Positon of card is {result}")

# #--------------------------------------------------

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
    
# cards = list(range(1,101))
# number = 17
# result = locate_card(cards,number)

# if result == -1:
#     print(f'Number {number} not founded')
# else:
#     print(f'Number {number} was founded at position {result}')    



def locate_card(cards,query):
    lo,hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards,query,mid)
        if result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
        elif result == "founded":
            return mid
    return -1

def test_location(cards,query,mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "founded"
    elif cards[mid] < query:
        return "right"
    else:
        return "left"



cards = list(range(1,100000))
query = 78939
result = locate_card(cards,query)
if result == -1:
    print(f'Number {query} not founded')
else:
    print(f'Number {query} was founded at position {result + 1}')  