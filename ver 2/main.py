import com_API as api
import com_CLI as cli

while True:
    user_input = cli.screenTitle() # Single모드와 Multi모드 중 하나를 고릅니다.
    if user_input == 1:
        cli.screenSingleModeSetting() # Single모드 실행 전 환경설정
    elif user_input == 2:
        cli.screenMuitiModeSetting() # Muiti모드 실행 전 환경설정
    elif user_input == 3:
        cli.screenSettings() # 환경설정 메뉴
        continue
    
    api.playImageRepeat(cli.screenCategorySelect(cli.screenTypeSelect())) # type과 category 선택 후 이미지 재생