import random, sys

from chapter02.janken2 import player_move

wins = 0
loses = 0
ties = 0
player_move = input()
#ゲーム開始
while True:
    print(f"{wins}勝 {loses}敗　あいこ{ties}回")
    while True:
        print("ここは後回し")
        break


    computer_move = random.randint(1,3)

    if computer_move == player_move:
        print("あいこです")
        ties += 1
    else:
        if computer_move == "0":
            print("コンピュータ:グー", end = "")
            wins += 1
            if player_move == "1":
                print("あなた：チョキ　...あなたの負けです")
                loses += 1
            else:
                print("あなた：パー　...あなたの勝ちです")
                wins += 1
        elif computer_move =="1":
            print("コンピュータ:チョキ", end="")
            if player_move =="0":
                print("あなた：グー ...あなたの勝ちです")
                wins += 1
            else:
                print("あなた：パー　...あなたの負けです")
                loses += 1
        else:
            print("コンピュータ:パー", end="")
            if player_move =="0":
                print("あなた：グー　...あなたの負けです")
            else:
                print("あなた：チョキ　...あなたの勝ちです")


