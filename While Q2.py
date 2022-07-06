value = int(input("value: "))

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