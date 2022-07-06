value = int(input("value: "))

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