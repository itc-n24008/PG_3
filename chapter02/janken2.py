import random, sys

print('じゃんけんぽん！')

wins = 0
losses = 0
ties = 0

while True:  # メインゲームループ
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('rはグー,pはパー,sはチョキ,かqで終了！')

    player_move = input()

    if player_move == 'q':
        sys.exit()  # プログラム終了

    # 正しい入力チェック
    if player_move not in ['r', 'p', 's']:
        print('r,p,s,qのいずれかをだしてね！')
        continue  # ゲームループの先頭に戻る

    # プレイヤーの手を表示
    if player_move == 'r':
        print('グーをだした...')
    elif player_move == 'p':
        print('パーをだした...')
    elif player_move == 's':
        print('チョキをだした...')

    # コンピュータの手を決める
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('グー')
    elif random_number == 2:
        computer_move = 'p'
        print('パー')
    else:
        computer_move = 's'
        print('チョキ')

    # 勝敗判定
    if player_move == computer_move:
        print('引き分け！')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('勝ち！')
        wins += 1
    else:
        print('負け！')
        losses += 1
