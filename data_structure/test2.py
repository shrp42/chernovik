# Бинарный поиск - подходит для работы с большими базами данных

def test_location(cards,query,mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "Left"
        else:
            return "Founded"
    elif cards[mid] < query:
        return "Left"
    else:
        return "Right"
    
def locate_card(cards,query):
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards,query,mid)
        if result == "Founded":
            return mid
        elif result == "Left":
            hi = mid - 1 
        elif result == "Right":
            lo = mid + 1
    return -1

cards = [10,9,8,7,6,5,4,3,2,1]
query = 2
locate_card(cards,query)  