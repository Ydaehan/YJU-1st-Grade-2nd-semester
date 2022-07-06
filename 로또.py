import random
# random.random() 으로 하면 0 과 1 사이 랜덤 실수 반환
# 정수로 받으려면 random.randrange() 사용

overlap_check = []
num = random.randrange(1,46)

for count in range(6):
    while num in overlap_check: # 리스트에 특정 값이 있는지 확인
        if num in overlap_check: # 리스트에 특정 값이 있는지 확인
            num = random.randrange(1,46)    # for 문의 range 와 같이 첫 지정 수 이상  끝 지정 수 미만 까지
    print(num," ",end="")
    overlap_check.insert(0,num) # insert(a,b) a번째 위치에 b를 삽입함