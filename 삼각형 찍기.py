value = int(input("라인 넘버를 입력 하세요 (홀수):"))

for row in range(value):
    if row <= value/2:
        for col in range(row+1):
            print("*",end="")
    else:
        for col in range(value-row):
            print("*",end="")
    print()