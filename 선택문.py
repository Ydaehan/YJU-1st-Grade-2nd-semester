#  아래 프로그램을 Python 프로그래밍 언어를 사용해 작성하시오
#  1) 키보드로부터 정수 값 입력
#  2) “1” 이상의 값만 입력, “0” 이하의 값 입력 시 아래 Msg 출력 후 재입력
#  3) 현재 입력 횟수 출력 후 키보드 입력 값 화면에 출력
#  4) “짝수”or “양수” 출력
#  5) 3의 배수 또는 7의 배수이면 아래 Msg 출력
#  6) ‘20,000’ 입력 시 아래 Msg 출력 후 프로그램 종료
#  7) 출력 값은 반드시 아래 형식 준수
a = True
count_num = 1

while a == True:
    value = int(input())
    if value == 20000:
        print("이용해주셔서 감사합니다")
        a = False 
    elif value <= 0:
        print("1 이상의 양수를 입력해주세요")
    elif 1 <= value:
        print(count_num,"번째 입력 값은 = ",value)
        if value % 2 == 0 or value % 2 != 0:
            if value % 2 == 0:
                print("         짝수 입니다.")
            else:
                print("         홀수 입니다.")

            if value % 3 == 0:
                print("         3의 배수 입니다.")

            if value % 7 == 0:
                print("         7의 배수 입니다.")
        count_num += 1

