# 로또 만들기 복습
# 하나의 리스트에 계속 저장해서 2줄 이상 뽑을때 줄 마다 중복이 허용되지않게됨
# 하지만  줄 마다 는 중복이 가능해야함
# 리스트를 여러개로 쓰고 저장을해야하나?

import random # random 함수를 사용하기위해 불러옴

def order():
    if game == 0:
        print(game+1,"st game: ",end="")
    elif game == 1:
        print(game+1,"nd game: ",end="")
    elif game == 2:
        print(game+1,"rd game: ",end="")
    else :
        print(game+1,"th game: ",end="")


def Rotto():
    rotto_num = random.randrange(1,46)    # randrange(a,b) = > a이상 b 미만의 수중 랜덤으로 반환
    while rotto_num in rotto_list:
        if rotto_num in rotto_list:
            rotto_num = random.randrange(1,46)
    if rotto_num <= 9:
        print(rotto_num,"  ",end="")
    else:
        print(rotto_num," ",end="")
    rotto_list.append(rotto_num)        # 리스트.insert(a,b) => 리스트a위치에 b 값을 삽입
                                        # 리스트.append(a) => 리스트에 a 를 추가


# main
rotto_list = [] # 로또 리스트 = 중복 체크를 위한 임시 저장소
win_count = 0
myN_list = []

print("자동으로 출력 할 로또 게임 수를 입력 하세요. :")
game_count = int(input())
print()
while game_count <= 0 or game_count >=6:
    if game_count <= 0 or game_count >=6:
        print("1~5 사이 수를 입력하세요.")
        game_count = int(input())
    print()


print("       ♧♣♧ 로또 생성기 ♧♣♧")
print("---------------------------------")
for game in range(game_count):
    for count in range(6): 
        if count == 0:
            order()
        Rotto()
    print()
    print("---------------------------------")
    print()


for a in range(6):
    while True:
        myN = int(input("당첨 번호를 입력: "))
        if myN in myN_list:
            print("동일한 수를 입력하셧습니다.")
            print("재입력 하십시오.")
            continue
        elif myN <= 0 or myN >= 46:
            print("로또 번호는 1~45 까지 입니다.")
            print("재입력 하십시오.")
        else:
            break

    myN_list.append(myN)
    
    if myN in rotto_list:
        win_count+=1
print("맞은 개수 : ",win_count,"개")

# 당첨 갯수 에 따른 이벤트 출력
if win_count == 6:
    print("축하합니다. 1등입니다.")
elif win_count == 5:
    print("축하합니다. 2등입니다.")
elif win_count == 4:
    print("축하합니다. 3등입니다.")
elif win_count == 3:
    print("아쉽군요. 4등입니다.")
else :
    print("아쉽군요. 당첨 되지 못했습니다.")


