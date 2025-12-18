#星座を入力
name = ['山羊座','水瓶座','魚座','牡羊座','牡牛座',
        '双子座','蟹座','獅子座','乙女座','天秤座',
        '蠍座','射手座']

key = ["I keep ...(私は守る)","I solve ...（私は解明する)","I believe ...（私は信じる)",
       "I exist.(私は存在する)","I have ...(わたしは所有する)","I choose ...(私は選択する)",
       "I sense ...（私は感じる)","I will ...(私は～する)","I analyze ...（私は分析する)",
       "I balance ...（私はバランスをとる)","I want ...(私は要求する)","I experience ...(私は体験する)"
]

#誕生日を入力
tuki = int(input('生まれた月を入力してください。'))
nitizi = int(input('生まれた日を入力してください。'))

eiza = tuki
if tuki == 1 and nitizi >= 20:
    eiza +=1
elif tuki ==2 and nitizi >= 19:
    eiza +=1
elif tuki == 3 and nitizi >= 21:
    eiza += 1
elif tuki ==4 and nitizi >= 20:
    eiza +=1
elif tuki ==5 and nitizi >= 21:
    eiza +=1
elif tuki ==6 and nitizi >= 22:
    eiza +=1
elif tuki ==7 and nitizi >= 23:
    eiza +=1
elif tuki ==8 and nitizi >= 23:
    eiza +=1
elif tuki ==9 and nitizi >= 23:
    eiza +=1
elif tuki ==10 and nitizi >=24:
    eiza +=1
elif tuki ==11 and nitizi >= 23:
    eiza +=1
elif tuki ==12 and nitizi >= 22:
    eiza =1

print(f"あなたの星座は{eiza}です")
print(f"あなたのキーワードは{key[eiza]}です")