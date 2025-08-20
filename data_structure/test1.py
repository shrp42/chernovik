def locate_card(cards,query):
    position = 0 

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

    return -1
    
cards = [1,2,3,4,5,6,7,8,9]   
query = 6
result = locate_card(cards,query)
if result != -1:
    print(f"Card position is = {result + 1}")
else:
    print("Card not founded")