import com_API as api
import time
import os

#by VDoring. 2021.07.05
#메인화면을 출력하고 어떤 메뉴를 선택할 것인지에 대한 입력을 받습니다.
#리턴값: 1, 2, 3
def screenTitle():
    while True:
        os.system('mode con cols=40 lines=11')
        os.system('title ACv v2.0-CLI')

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
        print('[3] EXIT')
        user_input = input('= ')

        if user_input == '1':
            api.setDelayTime()
        elif user_input == '2':
            api.setBrowser()
        elif user_input == '3':
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
                    break
                elif user_input.lower() == 'n':
                    api.valApiCountUp('browser_changed')
                    break
                else:
                    print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.75)
            except:
                print('[!] Please enter \'y\' or \'n\'! [!]')
                time.sleep(0.75)
            os.system('cls')

    return
    

#by VDoring. 2021.07.05
#사진 다중 출력 모드의 세부옵션을 출력하고 선택하게 합니다.
#리턴값: 없음
def screenMuitiModeSetting():
    pass