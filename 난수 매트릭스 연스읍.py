import random

# N X N 매트리스 내 난수 발행
# N 값을 키보드로 부터 입력받아...... -> 확장성



randList = []
allRandList = []
sortingList = []
while True : # 1 ~ 50 사이 정수 중복 x 25 개 선택 하여 리스트 저장
    randNum = random.randint(1,50)
    # 5 개를 받고 sort 후 리스트안에 리스트로 넣기
    if randNum in randList :
        continue
    randList.append(randNum)
    if len(randList) == 25:
        break
randList.sort()
# 5 * 5 행 열 구분
count = 1
print("전체 난수 리스트")
for row in randList:
    print(row,"ㅣ",end="")
    allRandList.append(row)
    if count % 5 == 0 :
        sortingList.append(allRandList)
        allRandList = []
        print()
    count += 1
# 열    (세로)
print()
print("열")
for row in range(3):
    for col in range(len(sortingList)):
        if row == 0:
            if col == 0 :
                print("최소값"," ",end="")
            print(sortingList[row][col]," ",end="")   # 최소
        elif row == 1:
            if col == 0 :
                print("최대값"," ",end="")
            print(sortingList[len(sortingList) - 1][col]," ",end="")     #최대
        else:
            if col == 0 :
                print("중간값"," ",end="")
            print(sortingList[len(sortingList[row]) // 2][col]," ",end="") # 중간값 찾기
    print()
# 행    (가로)
print()
print("행")
for col in range(len(sortingList)) :
    print("최소값 ","최대값 ","중간값 ")
    print(" ",sortingList[col][0]," "*5,end="")                     # 최소
    print(sortingList[col][len(sortingList[col]) - 1]," "*5,end="") # 최대
    print(sortingList[col][(len(sortingList) - 1)//2]," "*5,end="") # 중간값 찾기
    print()
# 전체
print()
print("전체")
# 최소
print("최소값",sortingList[0][1])
# 최대
print("최대값",sortingList[len(sortingList) - 1][len(sortingList[4]) - 1])
# 중간값 찾기
print("중간값",sortingList[len(sortingList) // 2][len(sortingList) // 2])