# ADv ver2.0.1 - by VDoring

import com_API as api
import com_CLI as cli

while True:
    user_input = cli.screenTitle() # 사용자가 Single모드와 Multi모드 중 하나를 고른다.
    if user_input == 1:
        cli.screenSingleModeSetting() # Single모드를 실행하기 전에 필수적인 설정을 한다.
        api.playSingleImageRepeat(cli.screenCategorySelect(cli.screenTypeSelect())) # Image type과 category 선택 후 Image 플레이
    elif user_input == 2:
        cli.screenMultiModeSetting() # Multi모드를 실행하기 전에 필수적인 설정을 한다.
        api.playMultiImageRepeat(cli.screenCategorySelect(cli.screenTypeSelect())) # Image type과 category 선택 후 Image 플레이
    elif user_input == 3:
        cli.screenSettings() # 전체 환경설정 메뉴