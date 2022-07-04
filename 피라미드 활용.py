floor = int(input("floor :"))
# 사다리꼴 윗변 아랫변 비율 1:3
"""
for row in range(floor):
    for non in range(floor-row-1):
        print(" ",end="")
    for col in range(2*row+2*floor):
        if col == 0 or col == (2*row+2*floor)-1:
            print("*",end="")
        elif row == 0 :
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""

# 역 사다리꼴
"""
for R_row in range(floor,0,-1):
    for R_non in range(floor-R_row):
        print(" ",end="")
    for R_col in range(2*R_row+2*floor):
        if R_col == 0 or R_col == (2*R_row+2*floor)-1:
            print("*",end="")
        elif R_row == 1 or R_row == floor:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
# 두개 합치면 육각형
"""
# 윗 사다리꼴
for row in range(floor):
    for non in range(floor-row-1):
        print(" ",end="")
    for col in range(2*row+2*floor):
        if col == 0 or col == (2*row+2*floor)-1:
            print("*",end="")
        elif row == 0 :
            print("*",end="")
        else:
            print(" ",end="")
    print()
# 아래 사다리꼴

for R_row in range(floor-1,0,-1):
    for R_non in range(floor-R_row):
        print(" ",end="")
    for R_col in range(2*R_row+2*floor-2):
        if R_col == 0 or R_col == (2*R_row+2*floor)-3:
            print("*",end="")
        elif R_row == 1 or R_row == floor:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
# 팔각형
# 좀 이상함
"""
for row in range(floor):
    for non in range(floor-row-1):
        print(" ",end="")
    for col in range(2*row+2*floor):
        if col == 0 or col == (2*row+2*floor)-1:
            print("*",end="")
        elif row == 0 :
            print("*",end="")
        else:
            print(" ",end="")
    print()

for S_row in range(floor-2):
    for S_col in range(4*floor-2):
        if S_col == 0 or S_col == 4*floor-3:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for R_row in range(floor-1,0,-1):
    for R_non in range(floor-R_row):
        print(" ",end="")
    for R_col in range(2*R_row+2*floor-2):
        if R_col == 0 or R_col == (2*R_row+2*floor)-3:
            print("*",end="")
        elif R_row == 1 or R_row == floor:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""

# 정삼각형
"""
for a in range(floor):
    print(" "*(floor-a-1),end="")
    print("*"*(2*a+1))
"""

# 역 삼각형
"""
for b in range(floor):
    print(" "*b,end="")
    print("*"*(2*floor-2*b-1))
"""

# 3중 삼각형
# floor = 8 일때의 삼각형 출력
"""
for row in range(floor):
    for non in range(floor-row-1):
        print(" ",end="")
    for col in range(2*row+1):
        if row <= floor//2 -1:
            print("*",end="")
        elif 0<= col <= 2*row-floor or 2*row-(2*row-floor)<= col <= 2*row:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""

# 모래시계

for r_row in range(floor,1,-1):
    for r_non in range(floor-r_row):
        print(" ",end="")
    for r_col in range(2*r_row-1):
        print("*",end="")
    print()

for row in range(floor):
    for non in range(floor - row - 1):
        print(" ",end="")
    for col in range(2*row+1):
        print("*",end="")
    print()


# 마름모
"""
for a in range(floor): # value - 1을 여기 넣어도 가능
    for none_a in range(floor-a-1):
        print(" ",end="")
    for b in range(2*a+1):
        if b == 0 or b == 2*a:
            print("*",end="")
        else :
            print(" ",end="")
    print()

for c in range(floor-1,0,-1):
    for none_b in range(floor-c):
        print(" ",end="")
    for d in range(2*c-1):
        if d == 0 or d == 2*c-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""