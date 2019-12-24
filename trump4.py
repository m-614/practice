import random

def is_included(source,target):
    for x in target:
        flg = True
        for y in source:
            flg = y in x and flg
        if flg:
            return flg

    return False

marks = ['club', 'diamond', 'heart', 'spade']
numbers = range(1,14)
cards = [(m,n) for m in marks for n in numbers]

chosen_cards = []

for i in range(100000):
    a = random.sample(cards,4)
    chosen_cards.append(a)

result = [(mark, 1) for mark in marks]

if is_included(result, chosen_cards):
    print ('ok')