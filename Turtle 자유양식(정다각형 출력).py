from select import select
import turtle

myTurtle = turtle.Turtle()
# 메뉴 함수
def menu() :
    while True :
        print("-"*20)
        print("도형 그리기")
        print("1.시     작")
        print("2.종     료")
        print("원하시는 메뉴의 번호를 입력해주세요.")
        print("-"*20)
        select = int(input())
        if select == 1:
            return select       # select 인풋값이 1일때 리턴
        elif select < 1 or select > 2 :     # 범위 초과 error 후 다시 메뉴 출력
            print("선택 범위를 초과 하셧습니다.")
            print("menu로 돌아갑니다.")
            continue
        elif select == 2:
            return select       # select 인풋값이 2 일때 리턴
        print("-"*20)
# 다각형 변 개수받기
def inputmypolygon():
    while True:
        num = int(input("출력하고 싶은 다각형의 변의 개수 를 입력하세요."))
        if num <= 2 :
            print("3 이상 정수를 입력해주세요.")
            continue
        else:
            break
    return num      # 함수 끝날대 num 값을 리턴
# 다각형 변 개수에 따른 길이 조정
def polygonlength():
    for i in range(inputMyPolygon):
        myTurtle.right(360 / inputMyPolygon)
        if inputMyPolygon <= 20:    # 정이십각형 이하
            myTurtle.forward(50)    # 한 변 당 길이 50 설정
        elif inputMyPolygon <= 50:  # 정이십각형 이상 정오십각형 이하
            myTurtle.forward(30)    # 한 변 당 길이 30 설정 => 설정 안 할 시 캔버스 범위를 넘어 버림
        elif inputMyPolygon <= 100: # 정오십각형 이상 정백각형 이하
            myTurtle.forward(10)    # 한 변 당 길이 10 설정
        elif inputMyPolygon <= 350: # 정백각형 이상 정삼백오십각형 이하
            myTurtle.forward(5)     # 한 변 당 길이 5 설정
        else :                      # 그 외
            myTurtle.forward(1)     # 한 변 당 길이 1 설정
count = 0
myTurtle.screen.bgcolor("BLACK")# turtle 캔버스 배경 색 변경
while(True):    # 무한반복
    select = menu()             # 메뉴에서
    if select == 2:             # 2번을 입력 받아야만 종료 가능
        print("프로그램 종료")
        break
    # 전에 그린거 지우기
    if select == 1:
        if count == 1 :  # 처음실행시에는 이 코드가 실행되지않게 위 에 count 변수 선언 
            myTurtle.speed(0)           # 빠르게 지우기 위함 speed(x) ,x의 범위는 1 ~ 10 까지 이지만 10 초과 시 최대속도 and 
                                        # 0 일 시에도 최대속도 
            myTurtle.color("BLACK")     # 지우는 용도 이기때문에 배경색과 동일
            myTurtle.width(4)           # 터틀 너비 조정 얇게
            polygonlength()
            myTurtle.setposition(0,0)
        # 3 이상 입력 받기
        inputMyPolygon = inputmypolygon()
        # 다각형 그리기 공식
        myTurtle.color("RED")       # 배경색과 다른색 사용 색지정은 마음대로
        myTurtle.speed(5)           # 그리기 속도 지정 적당하게 5 하지만 반복수가 늘어날수록 느림
        myTurtle.width(4)           # 너비 조정
        polygonlength()
        count = 1                   # count = 1  => 지우기를 하기 위한 스위치 역할
