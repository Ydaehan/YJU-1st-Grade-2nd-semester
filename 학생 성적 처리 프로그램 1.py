# - 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 입력 값을 출력하는 프로그램을 함수를 이용하여 작성하라.
# - 함수 구성은 자유!
# - 학생 성적 관리 테이블 구조 예 -> 리스트를 이용하여 구성

# 메뉴
def menu(argDataN , argAllStuAvg):
    print("="*30)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print("현 입력 데이터 갯수 : ", argDataN)
    print("전체 학생 평균 값 : ", argAllStuAvg)
    print("="*30)
    inputSelect = int(input())
    return inputSelect

def studentData():
    inputValue  = int(input("학번을 입력하세요 : "))
    inputName   = input("이름을 입력하세요 : ")
    inputKor    = int(input("국어 성적을 입력하세요"))
    inputEng    = int(input("영어 성적을 입력하세요"))
    inputMath   = int(input("수학 성적을 입력하세요"))
    sum         = inputKor + inputEng + inputMath   # 합
    avg         = sum / 3                           # 평균 
    stuList     = ["ID : " + str(inputValue) + " Name : " + inputName + " Kor : " + str(inputKor) + " Eng : " + str(inputEng) + " math : " + str(inputMath) + " Sum : " + str(sum) + " avg : " + str(avg)]
    return stuList, avg

dataN       = 0 # 현 입력 데이터 갯수
allStuAvg   = 0 # 전체 학생 평균 값
allStuAvgSum= 0 # 전체 학생 평균 합
allStuData  = [] # 전체 학생 데이터 리스트
while True :
    # 학생 정보 및 성적 입력 받기
    select = menu(dataN, allStuAvg)
    if select == 1:
        dataN += 1
        data, stuAvg  = studentData()
        allStuData.append(data)
        allStuAvgSum += stuAvg
        allStuAvg = allStuAvgSum / dataN
    
    if select == 2:
        for index in range(len(allStuData)):
            print(allStuData[index])
    if select == 3:
        print("프로그램 종료")
        break
    