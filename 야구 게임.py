# random 함수 호출
import random
# 시도 횟수 변수 선언
tryCount = 0
out = 0 # out count 변수
randList = [] # 난수 3개 를 저장할 리스트 생성
# 0 ~ 9 사이의 정수 3개 난수로 생성
while True:
    randNum = random.randint(0,9)
    # 중복 값 발생 할 수 있음
    # 중복 값 배제
    if randNum not in randList:
        # 그 후 리스트에 저장
        randList.append(randNum)
    if len(randList) == 3:
        break
while True :
    # 시도 횟수 출력
    tryCount += 1
    print("시도 횟수:",tryCount) 
    # 키보드로 부터 0 ~ 9 사이 정수 3개 입력 받고 결과 값을 출력
    myList = [] # 입력 받은 수를 저장 할 리스트
    print("정수 3개를 입력하세요.")
    while True:
        inputNum = int(input()) # 0 ~ 9 사이 정수 입력
        if inputNum < 0 or inputNum > 9:
            print("0 ~ 9 사이 정수를 입력해주세요.")
            continue
        elif inputNum in myList:# 입력 값의 중복 값 배제
            print("이미 입력한 값 입니다. 다시 입력하세요.")
            continue
        else:
            myList.append(inputNum)
            if len(myList) == 3:
                break
    # strike ball out 판단
    # strike ball 선언 (out은 while 문 밖에 선언)
    strike = 0
    ball = 0
    # 리스트에서 값을 하나씩 불러와서 
    # 두 리스트의 값을 비교하고
    # 두 리스트의 인덱스 값을 표시할 변수 선언
    randIndex = 0
    # 두 리스트의 인덱스 (위치)값을 비교해서 판단 후
    for checkRandNum in randList:
        myIndex = 0 # 밑의 for 문을 반복후 나와서 다시돌때 초기화
        for checkMyNum in myList:
            if checkRandNum == checkMyNum and randIndex == myIndex:
                strike += 1
            elif checkRandNum == checkMyNum and randIndex != myIndex:
                ball += 1
            myIndex += 1
        randIndex += 1
    # strike ball 출력
    # strike ball count 가 둘 다 0 이면 outCount += 1
    if strike > 0 :
        print(strike,"strike")
    if ball > 0 :
        print(ball,"ball")
    if strike == 0 and ball == 0 : 
        out += 1
        print("OUT : 아웃",out,"번")
    
    # 시도 횟수 >= 5
    if tryCount >= 5:
        print("-"*20)
        print("게임 횟수 초과")
        print("아까비~~~~졌네용..")
        print("정답은:",end="")
        for value in randList:
            print(value," ",end="")
        print("입니다.")
        print("-"*20) 
        break
    # out == 2
    elif out == 2:
        print("-"*20)
        print("GAME OVER")
        print("2 Out 당했네요..")
        print("아까비~~~~졌네용..")
        print("정답은:",end="")
        for value in randList:
            print(value," ",end="")
        print("입니다.")
        print("-"*20) 
        break
    elif strike == 3 :
        print("-"*20)
        print("Win!!")
        print("축하합니다!")
        print("정답입니다!")
        print("정답은:",end="")
        for value in randList:
            print(value," ",end="")
        print("입니다.")
        print("-"*20)
        break
    # 이면 게임횟수 초과 or 2out 게임 오버

