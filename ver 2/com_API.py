import requests
import time
import os

image_delay_time = 2.0 # Single play mode에서 다음 사진을 보여주기까지의 지연시간

command_chrome_run = 'start chrome -incognito ' # 크롬 시크릿모드 실행 명령어
command_edge_run = 'start msedge -inprivate ' # 엣지 시크릿모드 실행 명령어
command_firefox_run = 'start firefox -private ' # 파이어폭스 시크릿모드 실행 명령어

current_run_browser_name = 'chrome' # 현재 사용 설정된 웹 브라우저 이름
is_edit_browser_name = 0 # 사용자가 웹 브라우저 설정 창을 본 휫수(설정 시도 휫수)

is_save_url_to_txt = 'y' # URL을 .txt파일에 저장할 것인지에 대한 여부
is_save_url_to_txt_syslog = 'y' # URL을 syslog.txt에 저장할 것인지에 대한 여부
current_txt_name = 'URLlist' # 사용자 지정 .txt 파일의 이름
is_edit_txt_info = 0 # 사용자가 .txt파일 설정 창을 본 휫수(설정 시도 휫수)

current_need_url_count = 60 #Multi 모드에서 몇장의 URL 개수가 필요한지 저장
original_current_need_url_count = 0 # current_need_url_count 변수 값 백업

#by VDoring. 2021.07.05
#com_API.py의 특정 변수의 값을 올립니다.
#매개변수: val_name=값을 올릴 변수를 나타내는 임의의 문장
#리턴값: 없음
def valApiCountUp(val_name):
    global is_edit_browser_name
    global is_edit_txt_info

    if val_name == 'browser_changed':
        is_edit_browser_name += 1
    elif val_name == 'txt_info_changed':
        is_edit_txt_info += 1


#by VDoring. 2021.07.05
#Single play mode에서 사진 전환시 지연 시간을 조정합니다.
#리턴값: 없음
def setDelayTime():
    global image_delay_time

    os.system('mode con cols=50 lines=11')

    while True:
        print('< Set image delay time >\n')
        print('unit of time: Seconds(0, 1, 2, 1.5, 2.5, etc..)')
        print('Current delay time: %f seconds'%image_delay_time)
        try:
            user_input = float(input('= '))

            if user_input >= 0:
                image_delay_time = user_input
                print('\nComplete. \nNow delay time: %f seconds.'%image_delay_time)
                time.sleep(1.15)
                return
            else:
                print('[!] Please enter a number! [!]')
                time.sleep(0.7)
                os.system('cls')
        except:
            print('[!] Please enter a number! [!]')
            time.sleep(0.7)
            os.system('cls')



#by VDoring. 2021.07.05
#사용할 웹 브라우저를 설정합니다.
#리턴값: 없음
def setBrowser():
    global current_run_browser_name
    global is_edit_browser_name

    os.system('mode con cols=50 lines=11')

    while True:
        print('< Set web browser >\n')
        print('Current web browser: %s'%current_run_browser_name)
        print('input \'chrome\' or \'edge\' or \'firefox\'.')
        user_input = input('= ')

        if user_input.lower() == 'chrome':
            current_run_browser_name = 'chrome'
            is_edit_browser_name += 1
            print('\nComplete. \nNow web browser: %s.'%current_run_browser_name.upper())
            time.sleep(1.15)
            return
        elif user_input.lower() == 'edge':
            current_run_browser_name = 'edge'
            is_edit_browser_name += 1
            print('\nComplete. \nNow web browser is %s.'%current_run_browser_name.upper())
            time.sleep(1.15)
            return
        elif user_input.lower() == 'firefox':
            current_run_browser_name = 'firefox'
            is_edit_browser_name += 1
            print('\nComplete. \nNow web browser is %s.'%current_run_browser_name.upper())
            time.sleep(1.15)
            return
        else:
            print('[!] Please correct enter a string! [!]')
            time.sleep(0.7)
            os.system('cls')


#by VDoring. 2021.07.05
#사용자 지정 .txt 파일의 이름을 설정하고, URL을 .txt파일에 저장할지에 대한 여부를 설정합니다.
#리턴값: 없음
def setSaveUrlToTxt():
    global current_txt_name
    global is_save_url_to_txt
    global is_save_url_to_txt_syslog
    global is_edit_txt_info

    os.system('mode con cols=50 lines=15')

    while True:
        print('< Set .txt file >\n')
        print('[1] Current (user).txt file name: %s'%current_txt_name)
        print('[2] Current save URL to (user).txt file: %s'%is_save_url_to_txt)
        print('[3] Current save URL to syslog.txt file: %s'%is_save_url_to_txt_syslog)
        print('\n[9] EXIT')
        user_input = input('= ')

        if user_input == '1':
            print('\nInput (user).txt file name.')
            user_custom_file_name = input('= ')
            current_txt_name = str(user_custom_file_name)
            is_edit_txt_info += 1
            print('\nNow (user).txt file name: %s'%current_txt_name)
            time.sleep(1.15)
            os.system('cls')
            continue
        elif user_input == '2':
            print('\nWhether to save the URL to a (user).txt file [y/n]')
            user_input = input('= ')
            try:
                if user_input.lower() == 'y':
                    is_save_url_to_txt = 'y'
                    is_edit_txt_info += 1
                    print('\nComplete. \nNow is \'%s\'.'%is_save_url_to_txt)
                    time.sleep(1.15)
                    os.system('cls')
                    continue
                elif user_input.lower() == 'n':
                    is_save_url_to_txt = 'n'
                    is_edit_txt_info += 1
                    print('\nComplete. \nNow is \'%s\'.'%is_save_url_to_txt)
                    time.sleep(1.15)
                    os.system('cls')
                    continue
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                    time.sleep(0.7)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
        elif user_input == '3':
            print('\nWhether to save the URL to a syslog.txt file [y/n]')
            user_input = input('= ')
            try:
                if user_input.lower() == 'y':
                    is_save_url_to_txt_syslog = 'y'
                    is_edit_txt_info += 1
                    print('\nComplete. \nNow is \'%s\'.'%is_save_url_to_txt_syslog)
                    time.sleep(1.15)
                    os.system('cls')
                    continue
                elif user_input.lower() == 'n':
                    is_save_url_to_txt_syslog = 'n'
                    is_edit_txt_info += 1
                    print('\nComplete. \nNow is \'%s\'.'%is_save_url_to_txt_syslog)
                    time.sleep(1.15)
                    os.system('cls')
                    continue
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                    time.sleep(0.7)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
        elif user_input == '9':
            return
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.7)
        os.system('cls')


#by VDoring. 2021.07.05
#Multi play mode에서 수집할 URL수를 설정할 수 있습니다.
#리턴값: 없음
def setNeedUrlCount():
    global current_need_url_count

    os.system('mode con cols=50 lines=11')

    while True:
        print('< Set URL play count >\n')
        print('How many URLs do you need?')
        print('Current URL count: %d'%current_need_url_count)

        try:
            user_input = int(input('= '))

            if user_input >= 1:
                current_need_url_count = user_input
                print('\nComplete. \nNow need URL count: %d'%current_need_url_count)
                time.sleep(1.15)
                return
            else:
                print('[!] Please enter a right number! [!]')
                time.sleep(0.7)
                os.system('cls')
        except:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.7)
        os.system('cls')



#by VDoring. 2021.07.05
#사용자가 선택한 이미지 type과 category에 맞는 단일 이미지를 연속으로 사용자가 지정한 브라우저를 통해 출력합니다.
#매개변수: user_image_info=사용자가 선택한 이미지 type과 category
#리턴값: 없음
def playSingleImageRepeat(user_image_info):
    os.system('mode con cols=50 lines=11')
    
    cnt = 0
    print('\n< if you want to stop,')
    print('\nclick this program window and press Ctrl+C >')

    if user_image_info == 'EXIT':
        return
    try:
        if user_image_info[:3] == 'SFW':
            while True:
                cnt += 1
                os.system('title Single mode playing.. ' + '[' + str(cnt) + ']')
                playSingleImage(user_image_info[:3], user_image_info[3:])
        elif user_image_info[:4] == 'NSFW':
            while True:
                cnt += 1
                os.system('title Single mode playing.. ' + '[' + str(cnt) + ']')
                playSingleImage(user_image_info[:4], user_image_info[4:])

    except KeyboardInterrupt:
        return


#by VDoring. 2021.07.14 updated.
#사용자가 선택한 이미지 type과 category에 맞는 단일 이미지를 사용자가 지정한 브라우저를 통해 출력합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#          user_image_category=사용자가 선택한 이미지 category
#리턴값: 없음
def playSingleImage(user_image_type, user_image_category):
    global image_delay_time
    global current_run_browser_name
    global command_chrome_run
    global command_edge_run
    global command_firefox_run
    
    image_url = 'https://api.waifu.pics/type/category' # API 원본 링크
    image_url = image_url.replace('type', user_image_type.lower()) # type를 사용자가 원하는 type 이름으로 교체
    image_url = image_url.replace('category', user_image_category.lower()) # category를 사용자가 원하는 category 이름으로 교체
    
    res = requests.get(image_url) # (이미지 URL 구하는데 약 0.5초 소요)
    image_url = res.text # API에서 받은 값을 text부분만 가지기
    
    if current_run_browser_name == 'chrome':
        os.system(command_chrome_run + image_url[8:-3]) # 받은 text 값 중 불필요한 문자를 잘라서 이미지 출력
    elif current_run_browser_name == 'edge':
        os.system(command_edge_run + image_url[8:-3]) # 받은 text 값 중 불필요한 문자를 잘라서 이미지 출력
    elif current_run_browser_name == 'firefox':
        os.system(command_firefox_run + image_url[8:-3]) # 받은 text 값 중 불필요한 문자를 잘라서 이미지 출력

    time.sleep(image_delay_time) # 사용자가 설정한 지연시간


#by VDoring. 2021.07.06
#사용자가 선택한 이미지 type과 category에 맞는 다수의 이미지를 연속으로 사용자가 지정한 브라우저를 통해 출력합니다.
#매개변수: user_image_info=사용자가 선택한 이미지 type과 category
#리턴값: 없음
def playMultiImageRepeat(user_image_info):
    if user_image_info == 'EXIT':
        return

    global current_need_url_count
    global original_current_need_url_count

    os.system('mode con cols=50 lines=11')

    original_current_need_url_count = current_need_url_count # 기존 변수 값 복원을 위해 따로 값을 저장
    repeat_tens = 0 # 전체 단위의 반복 휫수. 1당 이미지 30개를 담당.
    repeat_units = 0 # 개별 단위의 반복 휫수. 1당 이미지 1개를 담당.

    while True: # 사진 출력 반복 휫수 정하기
        if current_need_url_count >= 30: # 만약 사용자가 원하는 URL 개수가 30개 이상이라면
            repeat_tens += 1
            current_need_url_count -= 30
        else: # 만약 사용자가 원하는 URL 개수가 30개 이하라면
            repeat_units = current_need_url_count
            break

    print('\n< if you want to stop,')
    print('\nclick this program window and press Ctrl+C >')
    try:
        if user_image_info[:3] == 'SFW':
                playMultiImage(user_image_info[:3], user_image_info[3:], repeat_tens, repeat_units)
        elif user_image_info[:4] == 'NSFW':
                playMultiImage(user_image_info[:4], user_image_info[4:], repeat_tens, repeat_units)
        current_need_url_count = original_current_need_url_count # 기존 값 복구

    except KeyboardInterrupt:
        current_need_url_count = original_current_need_url_count # 기존 값 복구
        return

#by VDoring. 2021.07.14 updated.
#사용자가 선택한 이미지 type과 category에 맞는 다수의 이미지를 사용자가 지정한 브라우저를 통해 출력합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#          user_image_category=사용자가 선택한 이미지 category
#          repeat_tens=이미지 출력을 반복할 휫수. 1당 30개의 이미지 출력
#          repeat_units=이미지 출력을 반복할 휫수. 1당 1개의 이미지 출력
#리턴값: 없음
def playMultiImage(user_image_type, user_image_category, repeat_tens, repeat_units):
    global original_current_need_url_count
    global current_run_browser_name
    global command_chrome_run
    global command_edge_run
    global command_firefox_run
    
    all_url_token_list = [] # 갱신된 모든 이미지의 URL을 저장
    cnt = 0

    if current_run_browser_name == 'firefox': # 파이어폭스는 실행에 시간이 걸리므로 미리 실행시켜두어 새 창에 생성되는 오류를 방지한다.
        os.system(command_firefox_run)
        time.sleep(0.7)

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
        
        all_url_token_list += res_token_list # 새로 생성된 링크들을 추가

        if current_run_browser_name == 'chrome': # 현재 브라우저가 chrome일 경우
            if tens < repeat_tens:
                for link in res_token_list:
                    os.system(command_chrome_run + link)
                    cnt += 1
                    os.system('title Multi mode playing.. [' + str(cnt) + '/' + str(original_current_need_url_count) + ']')
            else:
                for i in range(repeat_units):
                    os.system(command_chrome_run + res_token_list[i])
                    cnt += 1
                    os.system('title Multi mode playing.. [' + str(cnt) + '/' + str(original_current_need_url_count) + ']')

        elif current_run_browser_name == 'edge': # 현재 브라우저가 edge일 경우
            if tens < repeat_tens:
                for link in res_token_list:
                    os.system(command_edge_run + link)
                    cnt += 1
                    os.system('title Multi mode playing.. [' + str(cnt) + '/' + str(original_current_need_url_count) + ']')
            else:
                for i in range(repeat_units):
                    os.system(command_edge_run + res_token_list[i])
                    cnt += 1
                    os.system('title Multi mode playing.. [' + str(cnt) + '/' + str(original_current_need_url_count) + ']')

        elif current_run_browser_name == 'firefox': # 현재 브라우저가 firefox일 경우
            if tens < repeat_tens:
                for link in res_token_list:
                    os.system(command_firefox_run + link)
                    cnt += 1
                    os.system('title Multi mode playing.. [' + str(cnt) + '/' + str(original_current_need_url_count) + ']')
            else:
                for i in range(repeat_units):
                    os.system(command_firefox_run + res_token_list[i])
                    cnt += 1
                    os.system('title Multi mode playing.. [' + str(cnt) + '/' + str(original_current_need_url_count) + ']')

    writeTxtFile(all_url_token_list, repeat_tens, repeat_units) # .txt파일에 이미지 URL 작성


#by VDoring. 2021.07.06
#이미지의 URL을 syslog.txt(시스템로그용)와 유저의 .txt파일에 저장합니다.
#매개변수: all_url_list=(Multi play mode에서 생성된)모든 URL 리스트
#          repeat_tens=이미지 URL 기록을 반복할 휫수. 1당 30개의 이미지 URL을 작성할 수 있음
#          repeat_units=이미지 URL 기록을 반복할 휫수. 1당 1개의 이미지 URL을 작성할 수 있음
#리턴값: 없음
def writeTxtFile(all_url_list, repeat_tens, repeat_units):
    global is_save_url_to_txt
    global is_save_url_to_txt_syslog
    global current_txt_name
    global is_edit_txt_info

    user_txt_name = current_txt_name + '.txt' # 사용자 지정 .txt 파일
    sys_txt_name = 'syslog.txt' # 시스템 로그용 .txt 파일

    url_write_count = (repeat_tens * 30) + repeat_units # 리스트에서 URL을 꺼내서 쓸 휫수

# 사용자 .txt파일
    if is_save_url_to_txt == 'y':
        if os.path.isfile(user_txt_name): # 사용자 .txt파일
            f1 = open(user_txt_name, 'a') # 사용자 .txt파일 내용 추가 모드
        else:
            f1 = open(user_txt_name, 'w') # 사용자 .txt파일 새로(new) 작성 모드
        for i in range(url_write_count):
            data = all_url_list[i] + '\n'
            f1.write(data)
        f1.close()

# 시스템 .txt파일
    if is_save_url_to_txt_syslog == 'y':
        if os.path.isfile(sys_txt_name):
            f2 = open(sys_txt_name, 'a') # 시스템 .txt파일 내용 추가 모드
        else:
            f2 = open(sys_txt_name, 'w') # 시스템 .txt파일 새로(new) 작성 모드
        for i in range(url_write_count):
            data = '[' + str(i+1) + ']  ' + all_url_list[i] + '\n'
            f2.write(data)
        f2.close()