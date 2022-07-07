import random
rList = []
count = 1
valueSum = 0
# 1 ~ 20 사이 정수중 난수 값 20개 생성
for randNum in range(20):
    rList.append(random.randint(1,20))

# 랜덤 값 출력
print("랜덤 값 :")
for randValue in rList:
    print("\t",randValue,end="")
    if count % 10 == 0 : 
        print()
    count += 1

# 리스트 복사
copyList = rList.copy()

# 최소 값
minNum = rList[0]
maxNum = rList[0]

for minValue in rList:
    if minValue < minNum:
        minNum = minValue
print("최소 값 :",minNum)

# 최대 값
for maxValue in rList:
    if maxValue > maxNum:
        maxNum = maxValue
print("최대 값 :",maxNum)

# 합계
for sValue in rList:
    valueSum += sValue
print("합계\t:",valueSum)

# 평균
avr = valueSum / len(rList)
print("평균\t:",avr)

# 중복 값 과 중복 회수 (중복 된 수만 출력)
checkRlist = []

for value in range(20):
    checkCount = 0
    if minNum in rList:
        while minNum in rList:
            rList.remove(minNum)
            checkCount += 1
    if checkCount > 1:
        checkRlist.append([minNum,checkCount])
    minNum += 1


print("중복 값\t중복 회수")
for cValue in checkRlist:
    for cNum in cValue:
        print(" ",cNum,"\t",end="")
    print()
# 구간 별 히스토그램
#  1 ~ 5 : *****
#  6 ~ 10 : ****
#  11 ~ 15 : *****
#  16 ~ 20 : ******

# 갯수 가 col
for row in copyList:
    for col in range(4):