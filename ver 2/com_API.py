import requests
import time
import os

image_delay_time = 2.0 # 다음 사진을 보여주기까지의 지연시간

command_chrome_run = 'start chrome -incognito ' # 크롬 시크릿모드 실행 명령어
command_edge_run = 'start msedge -inprivate ' # 엣지 시크릿모드 실행 명령어

current_run_browser_name = 'edge' # 현재 사용설정된 브라우저
is_run_browser_changed = 0 # 사용자가 브라우저 설정여부를 본 휫수

is_save_url_to_txt = 'y' # 현재 URL을 txt파일에 저장하는지에 대한 여부
current_txt_name = 'URLlist' # URL을 저장하는 txt파일의 이름
is_edit_txt_info = 0 # 사용자가 .txt파일 설정여부를 본 휫수

current_need_url_count = 60 #Multi 모드에서 몇장의 URL 개수가 필요한지 저장


#by VDoring. 2021.07.05
#com_API.py의 특정 변수의 값을 올립니다.
#매개변수: val_name=값을 올릴 변수를 나타내는 임의의 문장
#리턴값: 없음
def valApiCountUp(val_name):
    global is_run_browser_changed
    global is_edit_txt_info

    if val_name == 'browser_changed':
        is_run_browser_changed += 1
    elif val_name == 'txt_info_changed':
        is_edit_txt_info += 1


#by VDoring. 2021.07.05
#사진 전환시 지연 시간을 조정합니다.
#리턴값: 없음
def setDelayTime():
    global image_delay_time

    os.system('mode con cols=50 lines=11')

    while True:
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
            os.system('cls')



#by VDoring. 2021.07.05
#사용할 브라우저를 설정합니다.
#리턴값: 없음
def setBrowser():
    global current_run_browser_name
    global is_run_browser_changed

    os.system('mode con cols=50 lines=11')

    while True:
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
            os.system('cls')


#by VDoring. 2021.07.05
#.txt 파일의 이름을 설정하고, URL을 .txt파일에 저장할지에 대한 여부를 설정할 수 있습니다.
#리턴값: 없음
def setSaveUrlToTxt():
    global current_txt_name
    global is_save_url_to_txt
    global is_edit_txt_info

    os.system('mode con cols=50 lines=11')

    while True:
        print('< Set .txt file >')
        print('[1] File name: %s'%current_txt_name)
        print('[2] \'Save URL to .txt file\' mode: %s'%is_save_url_to_txt)
        print('[3] EXIT')
        user_input = input('= ')

        if user_input == '1':
            print('\nInput .txt file name')
            user_custom_file_name = input('= ')
            current_txt_name = str(user_custom_file_name)
            is_edit_txt_info += 1
            print('Now .txt file name: %s'%current_txt_name)
            time.sleep(1.25)
            os.system('cls')
            continue
        elif user_input == '2':
            print('\nWhether to save the URL to a .txt file [y/n]')
            user_input = input('= ')
            try:
                if user_input.lower() == 'y':
                    is_save_url_to_txt = 'y'
                    is_edit_txt_info += 1
                    print('Complete. Now is \'%s\''%is_save_url_to_txt)
                    time.sleep(1.25)
                    os.system('cls')
                    continue
                elif user_input.lower() == 'n':
                    is_save_url_to_txt = 'n'
                    is_edit_txt_info += 1
                    print('Complete. Now is \'%s\''%is_save_url_to_txt)
                    time.sleep(1.25)
                    os.system('cls')
                    continue
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                    time.sleep(0.75)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.75)
        elif user_input == '3':
            return
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.75)
        os.system('cls')


#by VDoring. 2021.07.05
#Multi 모드에서 수집할 URL수를 설정할 수 있습니다.
#매개변수: url_count=수집할 URL 개수
#리턴값: 없음
def setNeedUrlCount(url_count):
    global current_need_url_count

    try:
        current_need_url_count = url_count
        print('Complete. Now need URL count is %d'%current_need_url_count)
        time.sleep(1.25)
        return
    except:
        print('[!] ERROR [!]')
        time.sleep(1.5)
        return



#by VDoring. 2021.07.05
#사용자가 선택한 이미지 type과 category에 맞는 단일 이미지를 연속으로 출력합니다.
#매개변수: user_image_info=사용자가 선택한 이미지 type과 category
#리턴값: 없음
def playSingleImageRepeat(user_image_info):
    os.system('mode con cols=40 lines=11')
    
    print('\n< if you want to stop, press Ctrl+C >')
    try:
        if user_image_info[:3] == 'SFW':
            while True:
                playSingleImage(user_image_info[:3], user_image_info[3:])
        elif user_image_info[:4] == 'NSFW':
            while True:
                playSingleImage(user_image_info[:4], user_image_info[4:])

    except KeyboardInterrupt:
        return


#by VDoring. 2021.07.05
#사용자가 선택한 이미지 type과 category에 맞는 단일 이미지를 출력합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#          user_image_category=사용자가 선택한 이미지 category
#리턴값: 없음
def playSingleImage(user_image_type, user_image_category):
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


#by VDoring. 2021.07.06
#사용자가 선택한 이미지 type과 category에 맞는 다수의 이미지를 연속으로 출력합니다.
#매개변수: user_image_info=사용자가 선택한 이미지 type과 category
#리턴값: 없음
def playMultiImageRepeat(user_image_info):
    global current_need_url_count

    os.system('mode con cols=40 lines=11')

    original_current_need_url_count = current_need_url_count # 값 복원을 위해 기존 변수 값 저장
    repeat_tens = 0 # 전체 단위의 반복 휫수
    repeat_units = 0 # 개별 단위의 반복 휫수
    while True: # 사진 출력 반복 휫수 정하기
        if current_need_url_count >= 30:
            repeat_tens += 1
            current_need_url_count -= 30
        else:
            repeat_units = current_need_url_count
            break

    print('\n< if you want to stop, press Ctrl+C >')
    try:
        if user_image_info[:3] == 'SFW':
                playMultiImage(user_image_info[:3], user_image_info[3:], repeat_tens, repeat_units)
        elif user_image_info[:4] == 'NSFW':
                playMultiImage(user_image_info[:4], user_image_info[4:], repeat_tens, repeat_units)
        current_need_url_count = original_current_need_url_count # 기존 값 복구

    except KeyboardInterrupt:
        current_need_url_count = original_current_need_url_count # 기존 값 복구
        return

#by VDoring. 2021.07.06
#사용자가 선택한 이미지 type과 category에 맞는 다수의 이미지를 출력합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#          user_image_category=사용자가 선택한 이미지 category
#          repeat_tens=이미지 출력을 반복할 휫수. 1당 30개의 이미지 출력
#          repeat_units=이미지 출력을 반복할 휫수. 1당 1개의 이미지 출력
#리턴값: 없음
def playMultiImage(user_image_type, user_image_category, repeat_tens, repeat_units):
    global image_delay_time
    global current_run_browser_name
    global command_chrome_run
    global command_edge_run
    
    for tens in range(repeat_tens+1):
        image_url = 'https://api.waifu.pics/many/type/category'
        image_url = image_url.replace('type', user_image_type.lower())
        image_url = image_url.replace('category', user_image_category.lower())
        
        data = {'param':''}
        res_list = requests.post(image_url, data=data)
        
        res_process_list = res_list.text[10:-3] # 리스트를 만드는데 불필요한 부분 제거
        res_process_list = res_process_list.replace('\"','') # " 를 제거

        res_token_list = [] # 각각의 링크로 나눠진 것을 저장하는 리스트
        res_token_list = res_process_list.split(',') # ,를 기준으로 문자열을 나눠서 리스트에 저장
        
        if current_run_browser_name == 'chrome':
            if tens < repeat_tens:
                for link in res_token_list:
                    os.system(command_chrome_run + link)
            else:
                for i in range(repeat_units):
                    os.system(command_chrome_run + res_token_list[i])
        elif current_run_browser_name == 'edge':
            if tens < repeat_tens:
                for link in res_token_list:
                    os.system(command_edge_run + link)
            else:
                for i in range(repeat_units):
                    os.system(command_edge_run + res_token_list[i])