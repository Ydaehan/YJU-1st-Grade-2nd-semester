# 야구게임
# 난수를 받아오기 위해서 random 함수 사용 import random
import random
# 게임 시작 시 0~9사이 정수중 3개의 난수를 받아와서 리스트로 저장
randomNumList = []
while True :
    randomNum = random.randint(0,9)
    if randomNum not in randomNumList :
        randomNumList.append(randomNum)
        if len(randomNumList) == 3:
            break
# 중복 허용 x
out = 0 # out 은 게임당 한번만 사용 함으로 초기화 x
# 시도 횟수 출력
tryCount = 0
# 정답을 알려줄때 사용할 함수
def result() :
    for result in randomNumList:
        print(result," ",end="")
while True :
    # 플레이어의 입력 값을 3개 받음 => 중복 x + 0~9 범위가 아닌 수 저장 x 
    # 플레이어 리스트 또한 게임 시도 때마다 초기화 시켜줘야한다.
    playerList = []
    tryCount += 1
    # 시도 횟수는 총 4번 주어짐 == 5번째 넘어가는 순간 횟수초과로 인한 GAMEOVER msg 출력후 종료
    if tryCount >= 5:
        print("아쉽네요.시도 횟수를 초과 하셧습니다.")
        print("-"*5,"GAME OVER","-"*5)
        print("정답은",end="")
        result()
        print("입니다.")
        break
    print()
    print("시도 횟수 :",tryCount)
    print("정수 3개를 입력하세요.(0~9/중복 불가)")
    while True :
        playerInputNum = int(input())
        if playerInputNum < 0 or playerInputNum > 9:
            print("입력된 값이 입력 범위를 초과 하셧습니다.(0~9사이의 정수)로 다시 입력해주십시오.")
            continue
        if playerInputNum not in playerList :
            playerList.append(playerInputNum)
            if len(playerList) == len(randomNumList) :
                break
        else:
            print("이미 입력된 수 입니다. 다시 입력 해주세요.")
    # strike ball out check
    strike = 0 # strike 와 ball 은 게임 시도 마다 초기화가 되어야 함으로
    ball = 0   # 선언을 반복문안에 하는 동시에 시도 마다 초기화 됨
    checkIndex = 0 
    for checkNum in randomNumList:
        playerIndex = 0 # playerIndex 는 플레이어의 값 위치 확인 시 사용 
                        # 체크가 끝나고 밑의 반복문을 탈출시 초기화 하여 다른 checkIndex와 비교 
        for playerNum in playerList:
            # strike == 플레이어의 값과 게임 시작 시 받은 난수의 값과 같으며 자리 위치가 같을때 +1
            if checkNum == playerNum and checkIndex == playerIndex:
                strike += 1
            # ball == 플레이어의 값은 같지만 자리위치가 서로 다를때 +1
            elif checkNum == playerNum and checkIndex != playerIndex:
                ball += 1
            playerIndex += 1
        checkIndex += 1
    # out
# 게임을 지거나 이길 경우 ( strike == 3 ) msg 출력 후 종료
    if strike == 0 and ball == 0 :
        out += 1    # out == strike 와 ball 의 카운트가 1도 없을때 out 처리 
                    # out 을 두번 받으면 GAMEOVER MSG 출력 후 프로그램 종료
        print("Out:","아웃",out,"번")
        if out == 2:
            print("아쉽네요.2 OUT 입니다.")
            print("-"*5,"GAME OVER","-"*5)
            print("정답은",end="")
            result()
            print("입니다.")
            break
    elif strike > 0 :
        print(strike,"strike"," ",end="")
        if strike == 3 :
            print()
            print("굉장하네요 정답입니다.")
            print("-"*5,"Winner!!","-"*5)
            print("정답은",end="")
            result()
            print("입니다.")
            break
    elif ball > 0 :
        print(ball,"ball")


