# 3 . 별출력
S = 5
for row in range(S):
    for col in range(S):
        if col <= row - 1 :
            print(" ",end="")
        else:
            print("*",end="")
    print()
