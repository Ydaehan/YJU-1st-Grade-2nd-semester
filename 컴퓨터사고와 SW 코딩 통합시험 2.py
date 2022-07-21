# 2. 정수 입력받아 양수면 양수 음수면 음수 0을 입력받으면
# 프로그램 종료
while True :
    inputNum = int(input("정수를 입력하세요."))
    if inputNum > 0 :
        print("양수 입니다.")
    elif inputNum < 0 :
        print("음수 입니다.")
    else :
        break
