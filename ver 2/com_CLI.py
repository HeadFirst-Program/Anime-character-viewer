import com_API as api
import time
import os

#by VDoring. 2021.07.05
#메인화면을 출력하고 어떤 메뉴를 선택할 것인지에 대한 입력을 받습니다.
#리턴값: 1, 2, 3
def screenTitle():
    while True:
        os.system('mode con cols=40 lines=11')
        os.system('title ACv v2.0')

        print('     < < Anime Character viewer > >')
        print('           v2.0 - by VDoring \n')
        print('[1] Single play')
        print('[2] Multi play')
        print('[3] Settings\n')
        user_input = input('= ')

        if user_input == '1':
            return 1
        elif user_input == '2':
            return 2
        elif user_input == '3':
            return 3
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.7)


#by VDoring. 2021.07.05
#모든 환경설정 메뉴를 볼 수 있고, 그 설정값을 수정할 수 있습니다.
#리턴값: 없음
def screenSettings():
    while True:
        os.system('cls')

        print('< Settings menu >\n')
        print('[1] Image time delay')
        print('[2] Web browser')
        print('[3] .txt file')
        print('\n[9] EXIT')
        user_input = input('= ')

        if user_input == '1':
            api.setDelayTime()
        elif user_input == '2':
            api.setBrowser()
        elif user_input == '3':
            api.setSaveUrlToTxt()
        elif user_input == '9':
            return
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.7)

#by VDoring. 2021.07.05
#사진 단일 출력 모드의 지연시간과 브라우저를 설정
#Single play mode시 다음 사진 출력까지의 지연시간과 사용할 웹 브라우저를 설정합니다. 이때 웹 브라우저는 최초 실행시에만 설정창이 나옵니다.
#리턴값: 없음
def screenSingleModeSetting():
    os.system('mode con cols=50 lines=11')

    while True:
        print('< Settings >\n')
        print('Current image delay time: %.3f seconds.'%api.image_delay_time)
        print('Do you want to change delay time? [y/n]')
        user_input = input('= ')

        try:
            if user_input.lower() == 'y':
                api.setDelayTime()
                break
            elif user_input.lower() == 'n':
                break
            else:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
        except:
            print('[!] Please enter \'y\' or \'n\'! [!]')
            time.sleep(0.7)
        os.system('cls')

    os.system('cls')

    if api.is_edit_browser_name == 0:
        while True:
            print('< Settings >\n')
            print('Current web browser is %s'%api.current_run_browser_name.upper())
            print('Do you want to change web browser? [y/n]')
            user_input = input('= ')

            try:
                if user_input.lower() == 'y':
                    api.setBrowser()
                    return
                elif user_input.lower() == 'n':
                    api.valApiCountUp('browser_changed')
                    return
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
            os.system('cls')
    

#by VDoring. 2021.07.06
#Multi play mode일시 .txt 파일 이름과 저장여부, 몇개의 URL이 필요한지 설정하며, 사용할 웹 브라우저를 설정합니다.
#                                                        이때 .txt파일 설정은 최초 실행시에만 설정창이 나옵니다.
#리턴값: 없음
def screenMultiModeSetting():
    os.system('mode con cols=50 lines=11')
    
    if api.is_edit_txt_info == 0:
        while True:
            print('< Settings >\n')
            print('Current .txt file name: %s'%api.current_txt_name)
            print('Current \'save URL to .txt file\' mode: %s'%api.is_save_url_to_txt)
            print('\nDo you want to enter .txt file settings? [y/n]')
            user_input = input('= ')

            try:
                if user_input.lower() == 'y':
                    api.setSaveUrlToTxt()
                    break
                elif user_input.lower() == 'n':
                    api.valApiCountUp('txt_info_changed')
                    break
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                    time.sleep(0.7)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
            os.system('cls')

    os.system('cls')

    while True:
        print('< Settings >\n')
        print('Current URL output count: %d'%api.current_need_url_count)
        print('Would you like to correct the count? [y/n]')
        user_input = input('= ')

        try:
            if user_input.lower() == 'y':
                api.setNeedUrlCount()
                break
            elif user_input.lower() == 'n':
                break
            else:
                print('[!] Please enter \'y\' or \'n\'! [!]')
            time.sleep(0.7)
        except:
            print('[!] Please enter \'y\' or \'n\'! [!]')
            time.sleep(0.7)
        os.system('cls')
        
    os.system('cls')

    if api.is_edit_browser_name == 0:
        while True:
            print('< Settings >\n')
            print('Current web browser is %s'%api.current_run_browser_name.upper())
            print('Do you want to change web browser? [y/n]')
            user_input = input('= ')

            try:
                if user_input.lower() == 'y':
                    api.setBrowser()
                    return
                elif user_input.lower() == 'n':
                    api.valApiCountUp('browser_changed')
                    return
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.7)
            os.system('cls')


#by VDoring. 2021.07.05
#사용자가 볼 Image type을 설정합니다.
#리턴값: SFW, NSFW
def screenTypeSelect():
    os.system('mode con cols=40 lines=11')

    while True:
        print('< Select type >\n')
        print('[1] SFW')
        print('[2] NSFW')
        print('\n[9] EXIT\n')
        user_input = input('= ')
        
        if user_input == '1':
            return 'SFW'
        elif user_input == '2':
            return 'NSFW'
        elif user_input == '9':
            return 'EXIT'
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.7)
            os.system('cls')



#by VDoring. 2021.07.05
#Image type에 속해있는 category를 사용자가 설정합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#리턴값: SFW/NSFW + 'waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug',
#                   'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile',
#                   'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill',
#                   'kick', 'happy', 'wink', 'poke', 'dance', 'cringe', 'trap', 'blowjob'
def screenCategorySelect(user_image_type):
    if user_image_type == 'EXIT':
        return 'EXIT'

    os.system('mode con cols=40 lines=36')

    sfw_category_list = ('waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug',
                    'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile',
                    'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill',
                    'kick', 'happy', 'wink', 'poke', 'dance', 'cringe')

    nsfw_category_list = ('waifu', 'neko', 'trap', 'blowjob')

    if user_image_type == 'SFW' :
        while True:
            print('< Select SFW category >\n')
            for i in range(1,len(sfw_category_list)+1):
                print('[%d] '%i, end='')
                print('%s'%sfw_category_list[i-1])
            user_input = input('= ')

            try:
                if user_input.isdigit() & ((int(user_input) >= 1) & (int(user_input) <= len(sfw_category_list))):
                    return 'SFW' + sfw_category_list[int(user_input)-1]
                else:
                    print('[!] Please enter a right number! [!]')
                    time.sleep(0.7)
            except:
                print('[!] Please enter a right number! [!]')
                time.sleep(0.7)
            os.system('cls')
    elif user_image_type == 'NSFW':
        while True:
            print('< Select NSFW category >\n')
            for i in range(1,len(nsfw_category_list)+1):
                print('[%d] '%i, end='')
                print('%s'%nsfw_category_list[i-1])
            user_input = input('= ')

            try:
                if user_input.isdigit() & ((int(user_input) >= 1) & (int(user_input) <= len(nsfw_category_list))):
                    return 'NSFW' + nsfw_category_list[int(user_input)-1]
                else:
                    print('[!] Please enter a right number! [!]')
                    time.sleep(0.7)
            except:
                print('[!] Please enter a right number! [!]')
                time.sleep(0.7)
            os.system('cls')
