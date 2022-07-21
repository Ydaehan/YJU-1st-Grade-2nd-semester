# 1. for 문으로 5개 정수 입력받아 
nSum = 0
N = 5
for a in range(N):
    print(a + 1,"번째 값 입력",end="")
    inputNum = int(input())
    nSum += inputNum
# 합계
print("합계 : ",nSum)
# 평균 출력
print("평균 : ",nSum / N)