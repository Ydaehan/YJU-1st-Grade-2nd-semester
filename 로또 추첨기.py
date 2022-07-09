# 로또 번호 랜덤값으로 6개 출력
import random
num = 0
rottoNum_list = []
index = 0
myN_list = []
sortMy_list = []
sortList = []

# 사용자 입력값 6개 받기 
# 자동 or 수동 선택
# 자동 이면 사용자 입력값 랜덤으로 출력
# 수동이면 직접입력해서 출력
def menu():
    print("당신의 로또 번호 출력 방법")
    print("-" * 20)
    print("1. 자동")
    print("2. 수동")
    print("-" * 20)

def manual():
    for numCount in range(len(rottoNum_list)):
        print("당신의 로또 번호를 입력하세요.")
        inputMyN = int(input())
        while True:
            if (inputMyN in myN_list) or inputMyN < 1 or inputMyN > 45:
                print("다시 입력하세요.(중복 or 범위 이탈)")
                inputMyN = int(input())
            else:
                break                 
        myN_list.append(inputMyN)

def automatic():
    global autoNum
    for a in range(6):
        autoNum = random.randint(1,45)
        while True:
            if autoNum in myN_list:
                autoNum = random.randint(1,45)
            else:
                myN_list.append(autoNum)
                break

# 로또 번호 중복값 제거
for a in range(6):
    num = random.randint(1,45)
    while True:
        if num in rottoNum_list:
            num = random.randint(1,45)
        else:
            rottoNum_list.append(num)
            break

menu()
inputMenu = int(input())
if inputMenu == 1 :
    automatic()
else :
    manual()

# 로또 번호 오름차순 정렬
minNum = rottoNum_list[0]
for num in rottoNum_list:
    if minNum >= num:
        minNum = num

while True:
    for sortcheck in rottoNum_list:
        if minNum == sortcheck:
            sortList.append(sortcheck)
            break
        else :
            continue
    minNum += 1
    if len(sortList) == 6 :
        minNum = 0
        break

print("로또 번호 : ",end="")
for rottoNum in sortList:
    print(rottoNum," ",end="")
print()

# 보너스 번호까지 1개 출력 
bonusRottoNum = random.randint(1,45)
while bonusRottoNum in rottoNum_list:
    bonusRottoNum = random.randint(1,45)
print("보너스 번호 :",bonusRottoNum)

# 내가 넣은 번호 오름 차순 정렬 (자동/수동)
while True:
    for sortcheck in myN_list:
        if minNum == sortcheck:
            sortMy_list.append(sortcheck)
            break
        else :
            continue
    minNum += 1
    if len(sortMy_list) == 6 :
        minNum == 0
        break

for myNum in sortMy_list:
    print(myNum," ",end="")

# 로또 번호랑 4개 부터 일치하면 5등 
# 로또 번호 5개랑 보너스 번호 1개 일치 - 2등
# 로도 번호 5개면 - 3등
# 로또 번호 랑 사용자 번호 인덱스 값 위치가 달라도 포함됨
winCount = 0
bonusWin = 0

for rotto in rottoNum_list:
    for myN in myN_list:
        if rotto == myN :
             winCount += 1
        elif rotto == bonusRottoNum :
             bonusWin += 1
print()
print(winCount)
print(bonusWin)

if winCount == 6 :
    print("1등 입니다.")
elif winCount == 5 and bonusWin == 1:
    print("2등 입니다.")
elif winCount == 5 :
    print("3등 입니다.")
elif winCount == 4 and bonusWin == 1:
    print("4등 입니다.")
elif winCount == 4 :
    print("5등 입니다.")
