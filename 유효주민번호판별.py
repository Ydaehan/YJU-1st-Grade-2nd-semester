# 주민 번호를 입력 받고
num = input("주민번호를 입력하세요.")
# 곱셈의 합 저장
checkSum = 0

# 유효한 주민 번호인지 판별
checkNum = 2 # 체크수 초기값
for index in range(len(num)-1): 
    if num[index].isdigit():                # num의 인덱스위치 값이 숫자이면
        checkSum += (int(num[index]) * checkNum) # 곱셈후 덧셈하여 합계 계산
        checkNum += 1                       # 체크 수 가 체크할때마다 1씩 더하면 곱셈
        if checkNum > 9 :
            checkNum = 2
    else:
        pass
        #마지막 숫자는 남기고 체크

# 체크 계산
# 단 마지막 값이 2자리일 경우 다시 10으로 나눈 나머지값을 구함

validationNum = 11 - (checkSum % 11)
if validationNum >= 10:
    validationNum = validationNum % 10

if int(num[13]) == validationNum :
    print("유효한 주민번호 입니다.")
else:
    print("유효하지 않은 주민번호 입니다.")