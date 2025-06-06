import re

with open('233.xml', encoding='utf-8') as f:
    data = f.read()

comments = re.findall('<d p="(.*?)">(.*?)</d>', data)
# print(len(comments))  # 3000
danmus = [','.join(item) for item in comments]
headers = ['stime', 'mode', 'size', 'color', 'date', 'pool', 'author', 'dbid', 'num','text']
headers = ','.join(headers)
danmus.insert(0, headers)

with open('danmus.csv', 'w', encoding='utf_8_sig') as f:
    f.writelines([line+'\n' for line in danmus])