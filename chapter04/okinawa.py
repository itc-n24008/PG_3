from re import search

okinawa = {"県花":"デイゴ", "県鳥":"イグチゲラ", "県魚":"タカサゴ",
           "県のお菓子":"こんぺん", "ソウルフード":"沖縄そば"}

print(okinawa.keys())

search=input("調べたのはなんですか　＞＞")

if search in okinawa:
    print(okinawa[search])
else:
    print("そのデータはありません")