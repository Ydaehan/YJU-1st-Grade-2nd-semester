# 학생들 성적을 입력 받아 리스트에 저장하고 입력값 출력
# 함수 구성 자유

# print menu
def menu(argDataN, argAllStuAvg):
    print("=" * 30)
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력 순)")
    print(" 3. 프로그램 종료")
    print()
    print("현 입력데이터 갯수 : ",argDataN)
    print("전체 학생 평균 값",argAllStuAvg)
    print("=" * 30)
    inputMyS = int(input())
    return inputMyS

# get Score of Subject
def getScoreOfSub():
    inputValueList = []
    scoreSum       = 0
    inputDataList = ["학번", "이름", "국어 성적", "영어 성적", "수학 성적"]
    for index in range(len(inputDataList)):
        print(inputDataList[index],"을 입력하세요.")
        inputValue = input()
        inputValueList.append(inputValue)   # 입력 값 리스트에 저장
    for index in range(2, 5):   # 국어 영어 수학 성적 합
        scoreSum += int(inputValueList[index])
    average = scoreSum / 3
    inputValueList.append(scoreSum)
    inputValueList.append(round(average, 2))
    allStuDataList.append(inputValueList)   # 전체 학생 데이터에 저장
    return average

allStuDataList  = []    # 전체 학생 데이터 리스트 
allStuAvg       = 0     # 전체 학생 평균
allStuAvgSum    = 0     # 전체 학생 평균 합
categoryList    = ["id", "name", "kor", "eng", "math", "sum", "avg"]    # 출력 데이터 양식
while True:
    select = menu(len(allStuDataList), allStuAvg)
    # select menu 1
    if   select == 1:
        allStuAvgSum += getScoreOfSub()
        allStuAvg     = round((allStuAvgSum / len(allStuDataList)), 2)
    # select menu 2
    elif select == 2:
        for stuDataList in allStuDataList:
            for iCount in range(len(stuDataList)):
                print(categoryList[iCount],":",stuDataList[iCount]," ",end="")
            print()
    # select menu 3 or input other menu value
    else : 
        print("프로그램 종료")
        break