def aisatsu(names,jikantai):
    if jikantai == 1:
        print(f'{names}さん、おはようございます')
    elif jikantai == 2:
        print(f'{names}さん、こんにちは')
    elif jikantai == 3:
        print(f'{names}さん、こんばんは')
    else:
        print(f"{names}さん、おやすみなさい")


name = input('お名前を入力してください >>')
print("朝：１　昼：２　晩：３　寝る前：３")
zikan = int(input('時間帯を入力してください >>'))
aisatsu(name,zikan)