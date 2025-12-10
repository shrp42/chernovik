#Линейный алгоритм - подходит для маленьких баз данных

def locate_card(cards,number):
    position = 0 

    while position < len(cards):
        if cards[position] == number:
            return position
        position += 1

    return -1
    
cards = [1,2,3,4,5,6,7,8,9]   
number = 6
result = locate_card(cards,number)
if result != -1:
    print(f"Card position is = {result + 1}")
else:
    print("Card not founded")

print('---Testing---')

tests = [
    {'input': {'cards': [2,3,3,4,4,4,42,52], 'number': 42}, 'output': 6},
    {'input': {'cards': [], 'number': 3}, 'output': -1},
    {'input': {'cards': [1,2,3,4,5,6], 'number': 9}, 'output': -1}
]
for i, test in enumerate(tests):
    result = locate_card(**test['input'])
    if result == test['output']:
        print(f'Test {i} passed')
    else:
        print(f"test {i} falied")