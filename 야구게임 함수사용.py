from itertools import count
import random
randList = []
triCount = 1
out = 0  # out 은 전체 게임중 2번 당하면 아웃임으로 while 바깥에 선언
# 난수 생성 및 정수 입력시 중복 및 범위이탈 방지
def overlapCheckList(list):
    # 게임 시작 시 난수 3개 리스트 저장 중복x
    if list == "randList":
        while len(randList) < 3 :
            randNum = random.randint(0,9)
            if randNum not in randList :
                randList.append(randNum)
        return list
    # 사용자에게서 정수 3개 리스트 저장 중복x 범위 초과 x
    elif list == "myList":
        while len(myList) < 3 :
            inputMyN = int(input())
            if inputMyN < 0 or inputMyN > 9 :
                print("정수 입력 범위를 초과. 재입력")
                continue
            elif inputMyN in myList:
                print("중복된 수 입력. 재입력")
                continue
            else :
                myList.append(inputMyN)
        return list
# strike ball
def checkBaseball(list):
    strike = 0
    ball = 0
    for index in range(len(randList)):
        if randList[index] == list[index] :
            strike += 1
        elif list[index] in randList :
            ball += 1
    if strike > 0 :
        print(strike,"strike ",end="")
    if ball > 0 :
        print(ball,"ball")
    return strike, ball

# out 판단 
def checkOutCount(strike,ball):
    global out
    if strike == 0 and ball == 0 :
        out += 1
        print("Out : ",out,"번")
        return out

# 정답 알려주는 문구
def correctAnswer():
    print("정답은",end="")
    for num in randList:
        print(num," ",end="")
    print("입니다.")
# 게임종료
def gameover():
    count = 0
    if strike >= 3:
        print()
        print("정답입니다.")
        print("수고하셧습니다.")
        correctAnswer()
        count = 1
    elif triCount >= 5:
        print()
        print("시도 횟수를 초과 하셨습니다.")
        print("\tGAME OVER")
        correctAnswer()
        count = 1
    elif out >= 2:
        print()
        print("2 Out 당하셧습니다.")
        print("\tGAME OVER")
        correctAnswer()
        count = 1
    return count

overlapCheckList("randList") 
while True :
    myList = []
    print("시도 횟수 :",triCount)
    print("정수 3개를 입력하세요.")
    overlapCheckList("myList")
    # strike ball out 비교
    strike, ball = checkBaseball(myList)
    checkOutCount(strike, ball)
    triCount += 1
    #gameover()
    if gameover() == 1:
        break