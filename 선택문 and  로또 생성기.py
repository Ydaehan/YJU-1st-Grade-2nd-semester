# 아래 프로그램을 Python 프로그래밍 언어를 사용해 작성하시오
#  1) 키보드로부터 정수 값 입력
#  2) “1” 이상의 값만 입력, “0” 이하의 값 입력 시 아래 Msg 출력 후 재입력
#  3) 현재 입력 횟수 출력 후 키보드 입력 값 화면에 출력 
#  4) “짝수”or “양수” 출력 
#  5) 3의 배수 또는 7의 배수이면 아래 Msg 출력
#  6) ‘20,000’ 입력 시 아래 Msg 출력 후 프로그램 종료
#  7) 출력 값은 반드시 아래 형식 준수
"""
count_num =  1

while True :
    value = int(input(""))
    if value <= 0:
        print("1이상 양수를 입력해주세요")
    elif value == 20000:
        print("이용해주셔서 감사합니다")
        break
    else :
        print (count_num,"번째 입력 값은 = ",value)
        if value % 2 == 0:
            print("             짝수 입니다.")
        else:
            print("             홀수 입니다.")
    
        if value % 3 == 0:
            print("             3의 배수 입니다.")
        if value % 7 == 0:
            print("             7의 배수 입니다.")
    count_num += 1
"""

# 로또 만들기 복습

import random

rotto_list = [] # 로또 리스트 = 중복 체크를 위한 임시 저장소

print("자동으로 출력 할 로또 게임 수를 입력 하세요. :")
game_count = int(input())
print()
while game_count <= 0 or game_count >=6:
    if game_count <= 0 or game_count >=6:
        print("1~5 사이 수를 입력하세요.")
        game_count = int(input())
    print()


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
    rotto_num = random.randrange(1,46)
    while rotto_num in rotto_list:
        if rotto_num in rotto_list:
            rotto_num = random.randrange(1,46)
    if rotto_num <= 9:
        print(rotto_num,"  ",end="")
    else:
        print(rotto_num," ",end="")
    rotto_list.append(rotto_num)

print("       ♧♣♧ 로또 생성기 ♧♣♧")
print("---------------------------------")
for game in range(game_count):
    for count in range(6):
        if count == 0:
            order()
        Rotto()
    print()
    print("---------------------------------")