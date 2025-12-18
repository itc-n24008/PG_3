name = ["平良","佐久田","田原"]
score = [0,0,0]

number=0
for i in range(3):
    score[number]=int(input(f"{name[i]}さんの点数を入力してください >>"))
    number+=1

for i in range(3):
    print()