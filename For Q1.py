value = int(input("value: "))

for a in range(1,value+1):
    for b in range(1,value+1):
        if b<=a:
            print(b,end="")
        else:
            print(" ",end="")
    print()