# 4. 1 ~ 100 까지 양의 정수 중 "3"이 포함된 정수만 출력
sNum = "3"
for num in range(1,101):
    if sNum in str(num):
        print(num)
