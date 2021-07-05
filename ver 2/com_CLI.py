import com_API as api
import time
import os

#by VDoring. 2021.07.05
#메인화면을 출력하고 어떤 메뉴를 선택할 것인지에 대한 입력을 받습니다.
#리턴값: 1, 2, 3
def screenTitle():
    while True:
        os.system('mode con cols=40 lines=11')
        os.system('title ACv v2.0-Dev.1')

        print('< Anime Character viewer >')
        print('Select the image output type.\n')
        print('[1] Single play mode')
        print('[2] Multi play mode')
        print('[3] Settings')
        user_input = input('= ')

        if user_input == '1':
            return 1
        elif user_input == '2':
            return 2
        elif user_input == '3':
            return 3
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.75)


#by VDoring. 2021.07.05
#환경설정을 할 수 있습니다
#리턴값: 없음
def screenSettings():
    while True:
        os.system('cls')

        print('< Settings menu >')
        print('[1] Image time delay')
        print('[2] Web browser')
        print('[3] .txt file')
        print('[4] EXIT')
        user_input = input('= ')

        if user_input == '1':
            api.setDelayTime()
        elif user_input == '2':
            api.setBrowser()
        elif user_input == '3':
            api.setSaveUrlToTxt()
        elif user_input == '4':
            return
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.75)

#by VDoring. 2021.07.05
#사진 단일 출력 모드의 지연시간과 브라우저를 설정
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
                time.sleep(0.75)
        except:
            print('[!] Please enter \'y\' or \'n\'! [!]')
            time.sleep(0.75)
        os.system('cls')

    os.system('cls')

    if api.is_run_browser_changed == 0:
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
                time.sleep(0.75)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.75)
            os.system('cls')
    

#by VDoring. 2021.07.05
#사진 다중 출력 모드의 세부옵션을 출력하고 선택하게 합니다.
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
                    time.sleep(0.75)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.75)
            os.system('cls')

    os.system('cls')

    while True:
        print('< Settings >\n')
        print('How many URLs do you need?')
        print('Current: %d'%api.current_need_url_count)
        try:
            user_input = int(input('= '))

            if user_input >= 1:
                api.setNeedUrlCount(user_input)
                return
            else:
                print('[!] Please enter a right number! [!]')
                time.sleep(0.75)
        except:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.75)
        os.system('cls')


#by VDoring. 2021.07.05
#SFW와 NSFW중 선택합니다.
#리턴값: SFW, NSFW
def screenTypeSelect():
    os.system('mode con cols=40 lines=11')

    while True:
        print('< Select type >')
        print('[1] SFW')
        print('[2] NSFW')
        user_input = input('= ')

        if user_input == '1':
            return 'SFW'
        elif user_input == '2':
            return 'NSFW'
        else:
            print('[!] Please enter a right number! [!]')
            time.sleep(0.75)
            os.system('cls')



#by VDoring. 2021.07.05
#SFW와 NSFW에 속해있는 카테고리를 선택합니다.
#매개변수: user_image_type=사용자가 선택한 이미지 type
#리턴값: SFW/NSFW + 'waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug',
#                   'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile',
#                   'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill',
#                   'kick', 'happy', 'wink', 'poke', 'dance', 'cringe', 'trap', 'blowjob'
def screenCategorySelect(user_image_type):
    os.system('mode con cols=40 lines=38')

    sfw_category_list = ('waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug',
                    'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile',
                    'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill',
                    'kick', 'happy', 'wink', 'poke', 'dance', 'cringe')

    nsfw_category_list = ('waifu', 'neko', 'trap', 'blowjob')

    if user_image_type == 'SFW' :
        while True:
            print('< Select SFW category >')
            for i in range(1,len(sfw_category_list)+1):
                print('[%d] '%i, end='')
                print('%s'%sfw_category_list[i-1])
            user_input = input('= ')

            if user_input.isdigit():
                return 'SFW' + sfw_category_list[int(user_input)-1]
            else:
                print('[!] Please enter a right number! [!]')
                time.sleep(0.75)
                os.system('cls')

    elif user_image_type == 'NSFW':
        while True:
            print('< Select NSFW category >')
            for i in range(1,len(nsfw_category_list)+1):
                print('[%d] '%i, end='')
                print('%s'%nsfw_category_list[i-1])
            user_input = input('= ')

            if user_input.isdigit():
                return 'NSFW' + nsfw_category_list[int(user_input)-1]
            else:
                print('[!] Please enter a right number! [!]')
                time.sleep(0.75)
                os.system('cls')

