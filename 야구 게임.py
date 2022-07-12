# 랜덤 함수를 사용하기 위해 랜덤호출
import random

randList = [] # 난수를 받을 리스트 선언
out = 0 # out 은 따로 초기화 할 필요없으므로 외부 선언

while True:
    # 0 ~ 9 사이 난수 3개 받기
    randNum = random.randint(0,9)
    # 난수 3개를 리스트에 저장
    # 중복 x
    if randNum not in randList :
        randList.append(randNum)
        if len(randList) == 3:
            break
    else:
        continue

# 시도 횟수 출력
tryCount = 1
while True:
    myList = [] # 시도 할때 마다 입력 수는 새로 받으므로 리스트를 초기화 
    print() # 결과 출력 과 겹칠수 있으므로 한줄 띄우기
    print("시도횟수:",tryCount)
# 키보드로 부터 0 - 9 사이 정수를 3개 입력받고
    print("정수 3개를 입력하세용~~~^^7")
    while True:
        inputMyN = int(input())
        if inputMyN < 0 or inputMyN > 9:
            # 입력값이 범위를 벗어났을때
            # 밑의 조건문을 실행 하지 않고 위로 올라감 
            print("정수는 0 ~ 9 사이 입니다. 다시 입력 하세요.")
            continue
        if inputMyN in myList: # 입력값이 입력리스트에 있는가 판단
            print("이미 입력한 수입니다. 다른 수를 입력하세요.")
            continue # 있으면 중복값이므로 continue
        else:
            myList.append(inputMyN) # 아니면 저장
            if len(myList) == 3:
                break
# 결과 값 출력 (strike ball out)
    strike = 0
    ball = 0 
    # 스트라이크 와 볼 은 게임 시도 때 마다 초기화 해야하기 때문에 
    # while 반복문 내에서 선언 겸 초기화
    randListIndex = 0 # 랜덤 리스트의 값을 들고 올때 그 값의 본래 위치 기억
    for randomBaseballNum in randList:
        myListIndex = 0 # 나의 리스트의 값을 들고 올때 그 값의 본래 위치 기억
        for myBaseballNum in myList:
            if myBaseballNum == randomBaseballNum and myListIndex == randListIndex:
                strike += 1
            # strike = 값이 같으면서 동시에 인덱스의 위치가 같으면 스트라이크
            elif myBaseballNum == randomBaseballNum and myListIndex != randListIndex:
                ball += 1
            # ball = 값은 같지만 다른인덱스 위치에 존재 할경우 볼
            myListIndex += 1
        randListIndex += 1
# strike 와 ball 출력
    if strike > 0 :
        print(strike, "strike", " ", end="")
        # 3스트라이크 시 게임 승리
        if strike == 3 : 
            print("축하합니다.")
            print("승리하셧습니다.")
            print("정답은:",end="")
            for answer in randList:
                print(answer," ",end="")
            print("입니다.")
            break
    if ball > 0:
        print(ball, "ball")
# strike ball 둘다 카운트가 되지 않은 아무것도 맞지않은 상황 = 아웃
    if strike == 0 and ball == 0:
        out += 1
        print("Out:","아웃",out,"번")
        # 아웃을 2번 당할경우 게임오버
        if out == 2 :
            print("2 Out!")
            print("아까비~~~~졌네용..")
            print("정답은:",end="")
            for answer in randList:
                print(answer," ",end="")
            print("입니다.")
            break
    tryCount += 1
    # 시도 횟수가 5 이상 일경우 게임오버
    if tryCount >= 5 :
        print("게임횟수 초과")
        print("아까비~~~~졌네용..")
        print("정답은:",end="")
        for answer in randList:
            print(answer," ",end="")
        print("입니다.")
        break
    


