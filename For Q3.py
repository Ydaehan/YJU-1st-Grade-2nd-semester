value = int(input("value: "))


for c in range(2):
    if c == 0:
        for a in range(value):
            for b in range(value):
                if a%2!=0 and b%2 != 0:
                    print(" ",end="")
                else :
                    print("*",end="")
            print()
    else:
        for c in range(value):
            for d in range(value):
                if c==d:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()
    print()