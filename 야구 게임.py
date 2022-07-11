# random 함수를 사용 하기 위해 random 호출
import random

# 난수값 리스트 선언
randNumList = []

# 중복 값이 안생기게 
# 정수의 범위는 0 ~ 9 사이
while True:
    randNum = random.randint(0,9)  # 0 ~ 9 사이 3개의 정수를 난수로 받기
    if randNum in randNumList:
        continue
    else:
        randNumList.append(randNum) # 받은 난수 3개를 리스트로 저장 (추후 사용)
        if len(randNumList) == 3:
            break

# 키보드로 부터 0 ~ 9 사이 정수 3개를 입력받고
# 결과 값 출력
# 중복 값 처리 


# 시도 횟수를 출력하기 위한 변수 선언
tryCount = 1
out = 0 # out 은 2번 당하면 GAME OVER 당함으로 
        # while문 밖에 선언
while True:
    myList = [] # 사용자가 입력한 수를 받을 리스트 선언 
    # 시도 할때 마다 초기화 시켜줘야 새로운 값을 입력 받음
    # 시도 횟수를 출력
    print("시도 횟수 :",tryCount)
    print("정수 3개를 입력하세용~~~^^7")
    while True:
        inputNum = int(input())
        if inputNum < 0 or inputNum > 9:
            print("입력 가능 범위가 아닙니다. 0 ~ 9 사이 정수를 입력하세요.")
            continue
        
        if inputNum not in myList:
            myList.append(inputNum)
            if len(myList) == 3:
                break
        else:
            print("중복 된 수 입니다. 다시 입력 하세요.")
            continue
        
        
    # strike ball out 판단
    # 출력
    # 인덱스 위치 비교를 위한 난수와 사용자 의 인덱스 변수 선언
    randIndex = 0
    myIndex = 0
    strike = 0 # strike 와 ball 은 반복을 하며 초기화를 
    ball = 0   # 시켜야 하기 때문에 while 문 내에 선언 하여 초기화
    for randValue in randNumList:
        myIndex = 0
        for myValue in myList:
            if myValue == randValue and myIndex == randIndex: # strike = 입력 값과 난수 값이 같으며 인덱스 위치가 같을때
                strike += 1
            elif myValue == randValue and myIndex != randIndex: # ball = 입력 값과 난수 값이 같은게 있지만 인덱스 위치가 다를 때
                ball += 1
            myIndex += 1 # 내부 반복문이 돌때 마다 myIndex + 1 
        randIndex += 1 # 외부 반복문이 돌때 마다 randIndex + 1
    # out은 strike 와 ball count 가 0 일때 count += 1
    # out 2번 당하면 msg 출력 후 게임오버
    if strike == 0 and ball == 0:
        out += 1
        if out == 2:
            print()
            print("-"*20)
            print("\tGAME OVER")
            print("\tOut 2번")
            print("아까비~~~졌네용")
            print("정답은 : ",end="")
            for value in randNumList:
                print(value," ",end="")
            print("입니다.")
            print("-"*20)
            break
        print("Out :","아웃",out,"번")
    # strike 출력    
    if strike > 0 :
        print(strike,"strike"," ",end="")
        if strike == 3:
            print()
            print("-"*20)
            print("WINNER!!")
            print("정답은 : ",end="")
            for value in randNumList:
                print(value," ",end="")
            print("입니다.")
            print("-"*20)
            break
    # ball 출력
    if ball > 0 :
        print(ball,"ball")
    tryCount += 1
    # 시도 횟수가 5회 되거나 그 이상일때 msg 출력 후 game over
    if tryCount >= 5:
        print()
        print("-"*20)
        print("\tGAME OVER")
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : ",end="")
        for value in randNumList:
            print(value," ",end="")
        print("입니다.")
        print("-"*20)
        break

