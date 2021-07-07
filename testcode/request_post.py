import requests
data = {'param':''}
res = requests.post('https://api.waifu.pics/many/sfw/neko', data=data)

str_text = res.text[10:-3] # 리스트를 만드는데 불필요한 부분 제거
str_text = str_text.replace('\"','') # "를 제거
#print(str_text)

l = []
l = str_text.split(',') # ,를 기준으로 문자열을 나눠서 리스트에 저장

# 확인 코드
for i in l:
    print(i)
print(len(l))
print(l)