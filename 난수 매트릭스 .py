import random
# N X N 매트릭스 내 난수 발행
# N 값을 키보드로 부터 입력받아
randList    = []    # 기존 리스트
colList     = []    # 행 리스트
RCList = []    # 정렬 리스트
while True:
    inputMatrix = int(input("N x N 형식으로 출력할 최대 범위(정수 N)를(을) 입력하세요."))
    if inputMatrix <= 1:
        print("error : 2 이상의 정수를 입력하세요.")
    else:
        break
while True: # 1 ~ n 사이 정수 중복 * (N x N)
    randNum = random.randint(1,50)
    # n개를 받고 sort후 리스트 안에 리스트로 넣기
    if randNum in randList :    # 중복 체크
        continue
    randList.append(randNum)
    if len(randList) == inputMatrix**2:
        break
# N * N 행 열 구분
count = 1
print("전체 난수 리스트")
for row in randList:
    print(row,"ㅣ",end="")
    colList.append(row)
    if count % inputMatrix == 0:
        RCList.append(colList)
        colList = []
        print()
    count += 1
# 열 (세로)
print()
print("열")
# 최소
print("최소값","ㅣ",end="")
for row in range(inputMatrix):
    minNum = 50
    for col in range(inputMatrix):
        if minNum >= RCList[col][row]:
            minNum = RCList[col][row]
    print(minNum," ",end="")
# 최대
print()
print("최대값","ㅣ",end="")
for row in range(inputMatrix):
    maxNum = 0
    for col in range(inputMatrix):
        if maxNum <= RCList[col][row]:
            maxNum = RCList[col][row]
    print(maxNum," ",end="")
# 중간
print()
print("중간값","ㅣ",end="")
for row in range(inputMatrix) :
    mList = [] # 행 리스트 정렬을 위함
    for col in range(inputMatrix) :
        mList.append(RCList[col][row])
    mList.sort()
    print(mList[(len(mList) - 1) // 2]," ",end="")
# 행
print()
print("행")
print(" 최소값","최대값","중간값")
# 최소 최대
for row in range(inputMatrix):
    minNum = 50
    maxNum = 0
    mList = [] # 행 리스트 정렬을 위함
    for col in range(inputMatrix):
        # 최소값
        if minNum >= RCList[row][col]:
            minNum = RCList[row][col]
        # 최대값
        if maxNum <= RCList[row][col]:
            maxNum = RCList[row][col]
        # 중간값 리스트
        mList.append(RCList[row][col])
    mList.sort()
    print(" ",minNum,"\t",end="")# 최소값
    print(maxNum,"\t",end="")# 최대값
    print(mList[(len(mList) - 1) // 2]) # 중간값
# 전체
print()
print("전체")
# 최소
print("최소값","ㅣ",end="")
allMinNum = 50
for row in randList:
    if allMinNum >= row :
        allMinNum = row
print(allMinNum)
# 최대
print("최대값","ㅣ",end="")
allMaxNum = 0
for row in randList:
    if allMaxNum <= row :
        allMaxNum = row
print(allMaxNum)
# 중간값
print("중간값","ㅣ",end="")
randList.sort()
print(randList[(len(randList) - 1) // 2])