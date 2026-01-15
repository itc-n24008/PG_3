import pathlib
import os

pname=input('調べるディレクトリ名を絶対パスで指名してください')
olist=os.listdir(pname)

p=pathlib.Path(pname)
if p.is_dir():
    olist = os.listdir(pname)
    for fo in olist:
        print(fo)
else:
    print(f"{pname}という")


for fo in plist:
    print(fo)