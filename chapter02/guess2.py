import random
secret_number = random.randint(1, 10)
print("１から10までの数を当ててください")
score = 5
# 6回聞く
for guesses_taken in range(1, 11):
    print("数を入力してください")
    guess = int(input())

    if guess < secret_number:
        print('あなたの推定数は小さいです。')
        score -= 1
    elif guess > secret_number:
        print('あなたの推定数は大きいです。')
        score -= 1
    else:
        score += 10
        break # あたり！

if guess == secret_number:
    print('あたり！' + str(guesses_taken) + '回で当たりました！')
    print('特典は'+str(score)+'点でした！')
else:
    print('残念。正解は' + str(secret_number) + 'でした。')