# https://pypi.org/project/selenium-requests/
# https://stackoverflow.com/questions/5660956/is-there-any-way-to-start-with-a-post-request-using-selenium
# https://waifu.pics/docs

# 셀레니움리퀘스트를 사용한 waifu.pics 30개 사진 받기 코드
from seleniumrequests import Chrome

webdriver = Chrome()
data = {'param':''}
res = webdriver.request('POST', 'https://api.waifu.pics/many/sfw/bonk', data=data)
#print(res)
print(res.text)
#print(res.content)

# requests를 사용한 waifu.pics 30개 사진 받기 코드
# import requests
# data = {'param':''}
# res = requests.post('https://api.waifu.pics/many/sfw/neko', data=data)
# print(res.text)