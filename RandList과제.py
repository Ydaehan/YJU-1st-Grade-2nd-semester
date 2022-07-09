import random

# 1~20 사이 양의 정수 중 난수 값 20개 생성 후 리스트 저장
rand_list = []
numCount = 1
randSum = 0
for loop in range(20):
    rand_list.append(random.randint(1,20))
print(rand_list) # 리스트 난수 확인용

print("랜덤 값 :")
for rlistValue in rand_list:
    print("\t",rlistValue,end="")
    if numCount % 10 == 0:
        print()
    numCount += 1

minNum = rand_list[0]
maxNum = rand_list[0]

# 최소 값
for num in rand_list:
    if num <= minNum:
        minNum = num
# 최대 값
for num in rand_list:
    if num >= maxNum:
        maxNum = num
# 합계
for num in rand_list:
    randSum += num

# 평균
randAvg = randSum / len(rand_list)
print("최소 값 :",minNum)
print("최대 값 :",maxNum)
print("합계\t:",randSum)
print("평균\t:",randAvg)

# 중복 값 중복 회수
print("중복 값"," ","중복 회수")
copyRand_list = rand_list.copy()
for value in range(len(rand_list)):
    overlapCount = 0
    if minNum in rand_list:
        while minNum in rand_list:
            rand_list.remove(minNum)
            overlapCount += 1
        if overlapCount >= 2:
            print(" "*2,minNum,"\t"," "*4,overlapCount)
    minNum += 1

# 히스토그램
aStar = 0
bStar = 0
cStar = 0
dStar = 0
for starValue in copyRand_list:
    if 1 <= starValue <= 5 :
        aStar += 1
    elif 6 <= starValue <= 10 :
        bStar += 1
    elif 11 <= starValue <= 15 :
        cStar += 1
    else :
        dStar += 1
print("구간별 히스토그램")
print(" 1 ~  5 :","*"*aStar)
print(" 6 ~ 10 :","*"*bStar)
print("11 ~ 15 :","*"*cStar)
print("16 ~ 20 :","*"*dStar)