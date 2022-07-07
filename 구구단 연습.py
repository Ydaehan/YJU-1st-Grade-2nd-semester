def menu():
    print("----------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("----------------")

while True:
    menu()
    inputValue = int(input())
    if inputValue == 1:
        print("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력")
        while True:
            inputNum = int(input())
            if inputNum <= 1 or inputNum >= 10:
                print("2~9사이 정수를 입력해주세요")
                continue
            else:
                for count in range(1,10):
                    print(inputNum,"X",count,"=",inputNum*count)
                break
    elif inputValue == 2:
        print("이용해주셔서 감사합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue