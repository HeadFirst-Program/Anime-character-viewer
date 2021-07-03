import com_api as api
import os
import time

#by VDoring. 2021.07.03
#시작화면을 출력하고 메뉴를 선택하게 합니다.
#리턴값: 1,2
def title():
    while True:
        os.system('mode con cols=40 lines=11') # 타이틀화면 화면 크기 설정
        os.system('title VDoring AC v1.0') # 윈도우타이틀 설정

        print('< Anime Girl viewer >\n')
        print('[1] SFW')
        print('[2] NSFW')
        print('= ', end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            if int(user_select) == 1: # 유저 입력값이 1일때
                return 1
            elif int(user_select) == 2: # 유저 입력값이 2일때
                return 2
            else: # 유저 입력값이 1이나 2가 아닐때
                print('[!] Choose from 1 or 2 [!]')
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)

#by VDoring. 2021.07.03
#sfw의 category 리스트를 출력하고 리스트 중 하나를 선택하게 합니다.
#리턴값: sfw_category의 요소들
def sfwSelect():
    sfw_category = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug',
                    'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile',
                    'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill',
                    'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']
    while True:
        os.system('mode con cols=40 lines=38') # 화면 크기 설정
        os.system('title Select SFW category..') # 윈도우타이틀 설정

        print('< Select category >\n')
        for i in range(1,len(sfw_category)+1):
            print('[%d]'%i, end='')
            print(sfw_category[i-1])
        print('\n= ', end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            for i in range(1,len(sfw_category)+1): # 리스트의 수만큼 반복
                if int(user_select) == i:
                    return sfw_category[i-1]
            else: # 유저 입력값이 카테코리의 수 밖에 있을때
                print('[!] Choose from 1~%d [!]'%len(sfw_category))
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)
                
#by VDoring. 2021.07.03
#nsfw의 category 리스트를 출력하고 리스트 중 하나를 선택하게 합니다.
#리턴값: nsfw_category의 요소들
def nsfwSelect():
    nsfw_category = ['waifu', 'neko', 'trap', 'blowjob']

    while True:
        os.system('mode con cols=40 lines=38') # 화면 크기 설정
        os.system('title Select NSFW category..') # 윈도우타이틀 설정

        print('< Select category >\n')
        for i in range(1,len(nsfw_category)+1):
            print('[%d]'%i, end='')
            print(nsfw_category[i-1])
        print('\n= ', end='')
        user_select = input()

        if user_select.isdigit(): # 유저 입력값이 숫자로만 이루어진 경우
            for i in range(1,len(nsfw_category)+1): # 리스트의 수만큼 반복
                if int(user_select) == i:
                    return nsfw_category[i-1]
            else: # 유저 입력값이 카테코리의 수 밖에 있을때
                print('[!] Choose from 1~%d [!]'%len(nsfw_category))
                time.sleep(0.75)
        else: # 입력값에 문자가 들어갔을 경우
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)