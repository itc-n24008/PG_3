import re

phone_number_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phone_number_regex.search('私の電話番号は098-862-5437')
print(f"電話番号が見つかりました：{mo.group()}")