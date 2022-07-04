# 홀수만 가능
value = int(input("value : "))
"""
value = int(input("value : "))

for row in range(value):
    if row <= value//2:
        for non in range(row):
            print(" ",end="")
    else:
        for non in range(value-row-1):
            print(" ",end="")
    if row <= value//2:
        for col in range(value-2*row):
            if col == 0 or col== value-2*row-1 or row == 0:
                print("*",end="")
            else:
                print(" ",end="")
    else:
        for col in range(2*row-(value-2)):
            if col == 0 or col == 2*row -(value-1) or row == value-1:
                print("*",end="")
            else:
                print(" ",end="")
    print()
"""


# 반으로 안가르고
"""
for a in range(value):
    for b in range(value):
        if a == b or a+b==value-1 or a == value-1 or a == 0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""