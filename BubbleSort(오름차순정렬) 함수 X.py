# N 개 정수 입력 받아 오름 차순 정리
N = 5   #입력 정수 갯수

inputValueList = [] # 입력 값 리스트

# 키보드로 부터 N 개의 정수를 입력 받아 리스트에 저장
for iCount in range(N):
    inputValue = int(input(str(iCount + 1) + "번째 입력값 : "))
    inputValueList.append(inputValue)
print(inputValueList)
# 리스트에 저장된 정수 값을 오름 차순 정렬
for a in range(N - 1):
    for b in range(N - a - 1):
        if inputValueList[b] > inputValueList[b + 1]:
            temp = inputValueList[b + 1]
            inputValueList[b + 1] = inputValueList[b]
            inputValueList[b] = temp
# 리스트 값 출력
print(inputValueList)