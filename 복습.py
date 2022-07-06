# while , for  반복문 복습

value = int(input("value: "))
# for 문
# Q1
"""
for a in range(1,value+1):
    for b in range(1,value+1):
        if b<=a:
            print(b,end="")
        else:
            print(" ",end="")
    print()
"""

# Q2
"""
for a in range(3):
    for b in range(value):
        for c in range(value):
            print("*",end="")
        print()
    print()
"""

# Q3
"""
for a in range(2):
    if a==0:
        for b in range(value):
            for c in range(value):
                if b%2!=0 and c%2!=0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()
    else :
        for d in range(value):
            for e in range(value):
                if d==e:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()
    print()
"""

# while 문
# Q1
"""
a=1

while a <= value:
    b=1
    while b <= a:
        print(b,end="")
        b+=1
    print()
    a+=1
"""

# Q2
"""
a=1
while a <= 3:
    b=1
    while b <= value:
        c=1
        while c <= value:
            print("*",end="")
            c+=1
        print()
        b+=1
    print()
    a+=1
"""

# Q3
"""
a = 1
while a <= 2:
    b=1
    while b <= value:
        c=1
        while c <= value:
            if a==1 and b%2 == 0 and c%2 == 0:
                print(" ",end="")
            elif a!=1 and b==c:
                print(" ",end="")
            else:
                print("*",end="")
            c+=1
        print()
        b+=1
    print()
    a+=1
"""

# 옆 면 피라미드

"""
for row in range(value):
    if row <= value / 2:
        for col in range(row+1):
            print("*",end="")
    else:
        for col_2 in range(value - row):
            print("*",end="")
    print()
"""