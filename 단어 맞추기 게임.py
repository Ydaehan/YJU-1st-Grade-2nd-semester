# 키보드로 부터 영단어 3개 입력 받아 리스트에 저장
# - 단어의 글자 범위 : 5 ~ 20 
# - 범위 이외 단어 입력 시 재입력
import random
# 단어 3개 입력 받기
def inputWord(argNum):
    for iCount in range(argNum):
        print(iCount + 1, "번째 단어를 입력 하세요.")
        inputWord = input()
        while len(inputWord) < 5 or 20 < len(inputWord) :
            print("5 이상 20 이하의 글자로 구성된 단어를 입력하세요.")
            inputWord = input()
        userWordList.append(inputWord)

# 입력 된 3개의 단어 중 한개 단어를 임의 선택
def selectWord(argList):
    select = random.randint(0, len(argList) - 1)
    return argList[select]

# 게임 시작
# Blind 처리 알파벳은 랜덤하게 선택
# ex) 지정된 단어가 starbucks 인 경우 [9 글자] 9/2 = 4.5 => 5(올림)
# 올림 알고리즘 직접 구현
def randBlindWord(argGameWord):
    # 선택 된 단어의 글자 중 50 % 를 Blind 처리
    # 올림 처리
    blindWordNum = len(argGameWord) / 2
    print(blindWordNum)
    decimalPoint = int(blindWordNum + 1) - blindWordNum
    if decimalPoint != 1:
        blindWordNum += decimalPoint
    print(blindWordNum)
    # 정수로 올림 처리 후 blind 처리
    while len(blindIndexList) < blindWordNum:
        a = random.randint(0, len(argGameWord) - 1)
        if a not in blindIndexList:
            blindIndexList.append(a)
    
# 알파벳을 입력 받고 매칭 시켜 블라인드 해제
def matchingStart(argGameWord,argTryCount):
    includeCount = 0    # 포함 카운트
    argTryCount += 1    # 시행 횟수
    print(argTryCount,"번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    # blind 처리
    for bIndex in range(len(argGameWord)):
        if bIndex in blindIndexList :
            print("_",end="")
        else :
            print(argGameWord[bIndex],end="")
    print()
    inputMyW = input()
    # 입력 알파벳과 일치한 알파벳이 있는지 확인
    for alphaIndex in range(len(argGameWord)):
        if argGameWord[alphaIndex] in inputMyW and alphaIndex in blindIndexList:
            # 일치 하며 블라인드 되있는 알파벳일 때 블라인드 해제
            blindIndexList.remove(alphaIndex)
            # 포함 카운트 1 증가
            includeCount += 1
    if includeCount >= 1:
        print("입력한 알파벳 단어 내 포함 : ",includeCount,"글자")
    else : 
        print("단어 내 포함 되지 않은 알파벳 입니다.")
    return argTryCount

userWordList    = []    # 유저 입력 단어 리스트       
blindIndexList  = []    # 블라인드 한 알파벳의 인덱스 리스트
tryCount        = 0     # 시도 횟수
inputWord(3)
gameWord = selectWord(userWordList)
print("단어 선택 완료 게임을 시작합니다. 선택된 단어 :",gameWord)
randBlindWord(gameWord)
# startGame
while True :
    tryCount = matchingStart(gameWord,tryCount)
    if len(blindIndexList) == 0:
        print("Clear - 선택된 단어 :",gameWord," 총 시도 횟수 :",tryCount)
        break




