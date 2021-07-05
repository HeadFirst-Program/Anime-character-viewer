import requests
import time
import os

image_delay_time = 2.0 # 다음 사진을 보여주기까지의 지연시간

command_chrome_run = 'start chrome -incognito ' # 크롬 시크릿모드 실행 명령어
command_edge_run = 'start msedge -inprivate ' # 엣지 시크릿모드 실행 명령어
current_run_browser_name = 'edge'
is_run_browser_changed = 0

#by VDoring. 2021.07.05
#com_API.py의 특정 변수의 값을 올립니다.
#매개변수: val_name=값을 올릴 변수의 이름
#리턴값: 없음
def valApiCountUp(val_name):
    global is_run_browser_changed

    if val_name == 'browser_changed':
        is_run_browser_changed += 1


#by VDoring. 2021.07.05
#사진 전환시 지연 시간을 조정합니다.
#리턴값: 없음
def setDelayTime():
    global image_delay_time

    os.system('mode con cols=50 lines=11')

    while True:
        os.system('cls')

        print('< Set image delay time >')
        print('unit of time: Seconds(0, 1, 2, 1.5, 2.5, etc..)')
        print('Current delay time: %f seconds'%image_delay_time)
        try:
            user_input = float(input('= '))

            if user_input >= 0:
                image_delay_time = user_input
                print('Complete. Now delay time is %f seconds.'%image_delay_time)
                time.sleep(1.25)
                return
        except:
            print('[!] Please enter a number! [!]')
            time.sleep(0.75)



#by VDoring. 2021.07.05
#사용할 브라우저를 설정합니다.
#리턴값: 없음
def setBrowser():
    global current_run_browser_name
    global is_run_browser_changed

    os.system('mode con cols=50 lines=11')

    while True:
        os.system('cls')

        print('< Set web browser >')
        print('Browser list: chrome, edge')
        print('Current web browser: %s'%current_run_browser_name)
        print('\ninput \'chrome\' or \'edge\'.')
        user_input = input('= ')

        if user_input.lower() == 'chrome':
            current_run_browser_name = 'chrome'
            is_run_browser_changed += 1
            print('Complete. Now browser is %s.'%current_run_browser_name.upper())
            time.sleep(1.25)
            return
        elif user_input.lower() == 'edge':
            current_run_browser_name = 'edge'
            is_run_browser_changed += 1
            print('Complete. Now browser is %s.'%current_run_browser_name.upper())
            time.sleep(1.25)
            return
        else:
            print('[!] Please correct enter a string! [!]')
            time.sleep(0.75)


#by VDoring. 2021.07.05
#사용자가 선택한 이미지 type과 category에 맞는 이미지를 연속으로 출력합니다.
#매개변수: user_image_info=사용자가 선택한 이미지 type과 category
#리턴값: 없음
def playImageRepeat(user_image_info):
    os.system('mode con cols=40 lines=11')
    
    print('\n< if you want to stop, press Ctrl+C >')
    try:
        if user_image_info[:3] == 'SFW':
            while True:
                playImage(user_image_info[:3], user_image_info[3:])
        elif user_image_info[:4] == 'NSFW':
            while True:
                playImage(user_image_info[:4], user_image_info[4:])

    except KeyboardInterrupt:
        return


#by VDoring. 2021.07.05
#사용자가 선택한 이미지 type과 category에 맞는 이미지를 출력합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#          user_image_category=사용자가 선택한 이미지 category
#리턴값: 없음
def playImage(user_image_type, user_image_category):
    global image_delay_time
    global current_run_browser_name
    global command_chrome_run
    global command_edge_run
    
    image_url = 'https://api.waifu.pics/type/category'
    image_url = image_url.replace('type', user_image_type.lower())
    image_url = image_url.replace('category', user_image_category.lower())

    res = requests.get(image_url) # 이미지 URL 구하는데 0.5초 걸린다
    image_url = res.text
    
    if current_run_browser_name == 'chrome':
        os.system(command_chrome_run + image_url[8:-3])
    elif current_run_browser_name == 'edge':
        os.system(command_edge_run + image_url[8:-3])

    time.sleep(image_delay_time)