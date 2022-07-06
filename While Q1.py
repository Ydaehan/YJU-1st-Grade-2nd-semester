value = int(input("value: "))

a = 1
while a <= value:
    b=1
    while b <= value:
        if b<=a:
            print(b,end="")
        else:
            print(" ",end="")
        b+=1
    print()
    a+=1
