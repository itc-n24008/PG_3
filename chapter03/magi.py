import random

def casper():
    kekka = random.randint(0,1)
    if kekka == 0:
        print('casper ... 可決')
    else:
        print('casper ... 否決')
    return kekka

def balthasar():
    kekka = random.randint(0, 1)
    if kekka == 0:
        print('balthasar ... 可決')
    else:
        print('balthasar ... 否決')
    return kekka

def melchior():
    kekka = random.randint(0, 1)
    if kekka == 0:
        print('melchior ... 可決')
    else:
        print('melchior ... 否決')
    return kekka



gidai = input('議題はなんですか >>')
print('審議に入ります')

result = casper()+balthasar()+melchior()
print('決議')
if result > 1:
    print(f'議題「{gidai}」は否決されました')
else:
    print(f'議題「{gidai}」は可決されました')
