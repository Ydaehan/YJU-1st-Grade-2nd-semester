def menu():
    print("----------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("----------------")
# 메뉴에서 "1" 선택 시 구구단 출력, "2" 인 경우 Msg. 출력 후 프로그램 종료
while True:
    # 메뉴 우선 출력 후 키보드 로 부터 정수 값 입력
    menu()
    inputValue = int(input())
    if inputValue == 1:
        #  “구구단 출력” 메뉴 선택 시 출력 할 단을 키보드로부터 입력
        #  출력 유효 단은 2 ~ 9
        print("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력")
        inputNum = int(input())
        if inputNum <= 1 or inputNum >= 10 :
            boolValue = True
            while boolValue == True: #  2 ~ 9단 이외의 값이 들어올 경우 Error Msg. 출력 후 재입력
                print("2~9사이 정수를 입력해주세요.")
                inputNum = int(input())
                if inputNum >= 2 and inputNum <= 9 :
                    boolValue = False
        if inputNum >= 2 or inputNum <= 9 :
            for num in range(1,10):
                print(inputNum,"X",num,"=",inputNum*num)
    elif inputValue == 2:
        print("이용해주셔서 감사합니다.")
        break
# 메뉴에서 “1” 또는 “2”이외의 값이 입력될 경우, Error Msg. 출력 후 재입력
    if inputValue >= 2 or inputValue <= 0:
        print("잘못 입력하셨습니다. 다시입력하세요.")
        


