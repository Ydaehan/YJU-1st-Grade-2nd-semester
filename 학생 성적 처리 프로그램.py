# 학생들 성적을 입력받아 리스트에 저장
# 입력 값을 출력하는 프로그램 작성
# 리스트를 이용하여 구성

# menu
def menu(argDataN,argAvg):
    print("="*30)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()
    print("현 입력 데이터 갯수 :",argDataN)
    print("전체 학생 평균 값   :",float(argAvg))
    print("="*30)
    inputSelect = int(input())
    return inputSelect

# 학생 성적 기입
def record():
    inputID     = int(input("학번을 입력하세요 : "))
    inputName   = input("이름을 입력하세요 : ")
    korRecord   = int(input("국어 성적을 입력하세요 : "))
    engRecord   = int(input("영어 성적을 입력하세요 : "))
    mathRecord  = int(input("수학 성적을 입력하세요 : "))
    stuSum      = korRecord + engRecord + mathRecord
    stuAvg      = stuSum / 3
    stuDataList = ["ID :" + str(inputID) + " Name :" + inputName + " Kor :" + str(korRecord) + " Eng :" + str(engRecord) + " Math :" + str(mathRecord) + " Sum :" + str(stuSum) + " Avg :" + str(round(stuAvg,1))]
    return stuDataList , stuAvg

# 메인
dataN       = 0     # 입력 데이터 갯수
allStuAvg   = 0     # 모든 학생 평균
allStuAvgSum= 0     # 모든 학생 평균 합
allDataList = []    # 모든 학생 점수 데이터 리스트

while True :
    select = menu(dataN, round(allStuAvg,2))
    if  select == 1:
        # 점수 기입 후 모든 학생리스트에 저장
        stuList, stuAvgSum = record()
        allDataList.append(stuList)
        allStuAvgSum    += stuAvgSum
        dataN           += 1
        allStuAvg   = (allStuAvgSum / dataN)
    elif select == 2:
        # 데이터 리스트 출력
        for iCount in range(len(allDataList)):
            print(allDataList[iCount])
    else:
        break
