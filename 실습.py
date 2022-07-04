"""
print("3 x 1 = 3")
print("3 x 2 = 6")
print("3 x 3 = 9")
"""

# 두 문장 출력 결과 이해해보기
# print("2 + 5 = 7")
# print("2 + 5 =", 2+5 )

# 앞 실습 내용을 응용하여 실행결과 나타내기
# 첫번째 활용
"""
print("9 x 1 = 9")
print("9 x 2 = 18")
print("9 x 3 = 27")
print("9 x 4 = 36")
print("9 x 5 = 45")
"""
# 두번째 활용
"""
print("9 x 1 =", 9*1)
print("9 x 2 =", 9*2)
print("9 x 3 =", 9*3)
print("9 x 4 =", 9*4)
print("9 x 5 =", 9*5)
"""
# 디버깅 테스트 예제문
"""
print("-------------------")

for value in range(1, 11) :
    
    print("value :", value)
    
    if value % 2 == 0 :
        print("2의 배수 입니다.")
    
print("-------------------")
"""

"""
# 키보드로 부터 첫번째 입력 값 저장
inpuValueA = input("첫번째 입력 값")

# 키보드로 부터 두번째 입력 값 저장
inpuValueB = input("두번째 입력 값")

# 입력 받은 두 개의 값에 대해 더하기 연산 실시
result = inpuValueA + inpuValueB

# 연산 결과 화면 출력
print(result)
"""
"""
################
# 정수  자료형 #
###############
temp_int = 2

print(type(temp_int))
# 출력 값 : <class 'int'>

################
# 실수  자료형 #
###############
temp_float = 1.5

print(type(temp_float))
# 출력 값 : <class 'float'>

################
# 문자  자료형 #
###############
temp_string_1 = "bar"
temp_string_2 = "foo"

print(type(temp_string_1), type(temp_string_2))
# 출력 값 : <class 'str'>, <class 'str'>
"""
"""
################
# Bool  자료형 #
###############
temp_bool_1 = True
temp_bool_2 = False

print(type(temp_bool_1), type(temp_bool_2))
# 출력 값 : <class 'bool'>, <class 'bool'>

# 흐름 제어 if else
if temp_bool_1 :
    print("temp_bool_1 = 참")
else :
    print("temp_bool_1 = 거짓")
if temp_bool_2 :
    print("temp_bool_2 = 참")
else :
    print("temp_bool_2 = 거짓")
"""
"""
# Truthy , Falsy 예제
temp_1 = 1  # 정수형 변수
temp_2 = -1 # 정수형 변수
temp_3 = 0  # 정수형 변수
temp_4 = -0 # 정수형 변수

if temp_1 :          # 1 -> Truthy 값
    print("참")      # 출력값
else :
    print("거짓")
    
if temp_2 :          # -1 -> Truthy 값
    print("참")      # 출력값
else :
    print("거짓")
    
if temp_3 :          # 0 -> Falsy 값
    print("참")     
else :
    print("거짓")    # 출력값
    
if temp_4 :          # -0 -> Falsy 값
    print("참")
else :
    print("거짓")    # 출력값
"""

"""
#자료형 별 Falsy 값
temp_1 = 0
temp_2 = 0.0
temp_3 = ""
temp_4 = None

if temp_1 :          # 0 -> Falsy 값
    print("참")      
else :
    print("거짓")    # 출력값
    
if temp_2 :          # 0.0 -> Falsy 값
    print("참")      
else :
    print("거짓")    # 출력값
    
if temp_3 :          # "" -> Falsy 값
    print("참")     
else :
    print("거짓")    # 출력값
    
if temp_4 :          # None -> Falsy 값
    print("참")
else :
    print("거짓")    # 출력값
"""


"""
################
# List  자료형 #
###############

temp_list = [10, 2, 2.5, "Test"]

print(temp_list[0] , temp_list[1] , temp_list[2] , temp_list[3])
#10, 2, 2.5, Test

temp_list[3] = 9
temp_list[2] = 8
temp_list[1] = 7
temp_list[0] = 6
print(temp_list[0] , temp_list[1] , temp_list[2] , temp_list[3])
# 6 7 8 9

temp_list[4] = 20  #error
"""

"""
error 가 발생한 이유는?
리스트 는 0 부터 시작하고 지정한 변수의 갯수를 n이라 치면
index 번호를 0 ~ n-1 까지 사용 가능
처음에 리스트 안의 변수를 4개로 지정했기 때문에
[0] / [1] / [2] / [3] 은 가능하지만 [4]는 없는 index 임으로 오류가 발생
"""

"""
# 실습 1
# 지구에서 프록시마 케타우리 별 까지  빛의 속도로 간다면 몇년이 걸릴까?

Toproxima = 40*(10**12)
LightSpeed = 3*(10**5)
EtoP = Toproxima / LightSpeed
Year = 3600*24*365
print(Toproxima)
print(LightSpeed)
print(EtoP)
print(Year)

print("지구와 프록시마 케타우리 별 까지:",EtoP / Year)
# 4.227972264501945 년
"""

#실습2
#아래와 같은 동작을 하는 프로그램을 작성하라
#키보드로 부터 문자입력
#입력값이 남자면 MAN / 여자면 WOMAN 출력

"""
inpuGender = input("성별을 입력 하세요:  ")
if inpuGender == "남자" :
    print("MAN")
if inpuGender == "여자" :
    print("WOMAN")
"""

#실습 3 
#아래와 같은 동작을 하는 프로그램을 작성하라
#키보드로 부터 문자입력
#입력 값이 < 0 이면 “음수” 출력
#입력 값이 > 0 이면 “양수” 출력

"""
inpuN = int(input("정수값을 입력 해 주세요.  "))

if inpuN < 0 :
    print("음수")
if inpuN > 0 :
    print("양수")
if inpuN == 0 :
    print("0")
"""


"""
# 두 개의 값을 입력받아 더한 값을 출력하는 함수 정의
def Add(argValueA, argValueB):
    # 입력 받은 두 개의 수를 더한 후 문자열로 변환
    result = str((argValueA + argValueB))
    # 출력 메시지 작성
    msg = "합계 : " + result
    # 함수 반환 값
    return msg


# 233라인에서 작성한 함수 호출
print(Add(2,3)) # 합계 : 5

# 233 라인에서 작성한 함수 호출
print(Add(4,5)) # 합계 : 9
"""

"""
name = "DH Yoo"

def printHelloMsg():
    print("Hello")
    print(name) # 함수 내에서 함수 밖에 선언되어 있는 변수(전역변수) 접근 가능
    #name = "Richard Yoo"
    position = "student" # position 변수의 생명주기?

printHelloMsg()

print(name)

#print(position) 변수의 생명주기로 260줄 함수가 호출후 종료되었을때 변수가 죽어 호출 불가
"""

"""
value = 10

def multiply10() :
    #global value #주석 처리 전/후 결과 값 비교
    
    value = value * 10
    
    return value 

print(multiply10())
"""

#실습 4
#화면에 "hello"를 출력하는 printHello 함수를 작성하라
"""
def printHello() :
    print("hello")
    
printHello()
"""

#실습 5
#세 개의 정수 값을 입력 받아 곱한 값을 반환하는 함수를 작성하라
"""
def multiply(argA, argB, argC) :
    argD = argA*argB*argC
    return argD 

value = multiply(1, 2, 3)

print(value) #출력값 6
"""

#실습 6
#특정 정수의 값이 짝수 이면 “짝수＂아니면 “홀수”를 출력하는 함수를 작성하라.

#입력 값의 홀,짝 여부 판별 후
#출력 : "짝수" or "홀수"

"""

def getEvenOdd(argValue) :

    if argValue % 2 == 0  : # 몫 -> // 나머지 -> % 나눗셈 / 연산자를 몰라 헤맴
        print("짝")
    else :
        print("홀")


getEvenOdd(2) # 결과값 짝수
getEvenOdd(3) # 결과값 홀수

"""

# 산술 연산자 -> 수를 계산하는 연산자
# 기본 사칙연산과 나머지(%) 또는 몫 구하기(//) , 지수(**)
"""
result_1 = 1 + 3.5
result_2 = 2 - 5.5
result_3 = 3 * 7
result_4 = 5 / 2

# 출력 값 : 4.5    -3.5    21.    2.5
print(result_1, result_2, result_3, result_4)

# 출력 값 : <class 'float'> <class 'float'> <class 'int'> <class 'int'>
print(type(result_1), type(result_2), type(result_3), type(result_4))
"""

# 몫(//), 나머지(%) 연산자
# // : 나누기 연산 후 몫 값만 반환

"""

result_1 = 3 // 2
result_2 = 3 / 2

# 출력 값 : 1    1.5
print(result_1, result_2)

# % : 나누기 연산 후 나머지 값 반환 -> Modulor 연산자
# 출력 값 : 0  1  2  0  1  2
for divisor in range(6):
    print(divisor%3)

# 나머지 연산은 특정 패턴을 찾기위해 번번하게 사용
# 예) 특정 반복문 내에서 3번째 반복마다 특정 명령어 실행
count = 1

for dan in range(2, 10) :
    for num in range(1, 10):
        print(dan, " X ", num, " = ", (dan*num))

    if count % 3 == 0:
        print("==================================")

    count += 1

"""

"""
# 지수 연산자 : **

# 2의 3승
result_1 = 2**3

# 결과 값 : 8
print(result_1)

# 결과 값 : 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
for value in range(11):
    print(2**value)

"""

# 비교 연산자 : 좌항과 우항의 값을 비교
# 비교 연산자 종류 : >, >=, <, <=, ==, !=

"""
print(3 > 4)            #false
print(2 > 2)            #false
print(2.0 >= 2)         #true
print(3 < 4)            #true
print(4 <= 4)           #true
print(1 == 1)           #true
print(1 != 2)           #true
print(True != False)    #false

print("a" > "c")        #false
"""



# 주어진 점수에 대해 A ~ F 등급으로 출력 프로그램
# if ~ elif ~ else 문 활용

"""
print("점수를 입력하면 등급이 나옵니다!")
record = input() # 활용 시 오류 발생 => type 이 str / str -> int type 변경 필요
"""

"""

record = 70

if record >= 90:
    print("A")
elif record >= 80:
    print("B")
elif record >= 70:
    print("C")
elif record >= 60:
    print("D")
else :
    print("F")
"""

# 논리 연산자 : 진리표를 활용한 연산 실시
# 논리 연산자 종류 : and or not

# and 연산자
# - 이항 연산자
# - 좌항과 우항의 값이 "참"일때만 참,
# - 그 이외에는 모두 거짓

"""
if 3 < 2 and 3 < 3 :
    print("T 1")

if 3 > 2 and 3 < 3 :
    print("T 2")

if 3 < 2 and 3 >= 3 :
    print("T 3")

if 3 > 2 and 3 >= 3 : # 좌항 우항 모두 True 값 임으로 위의 False 값을 가지는 if문들을 다 빠져나와 T4 만 출력
    print("T 4")

"""

# or 연산자
# - 이항 연산자
# - 좌항과 우항값 중 하나라도 "참"이면 참,
# - 그 이외에는 모두 거짓

"""
if 3 < 2 or 3 < 3 :
    print("T 1")

if 3 > 2 or 3 < 3 :
    print("T 2")

if 3 < 2 or 3 >= 3 :
    print("T 3")

if 3 < 2 or 3 >= 3 :
    print("T 4")
"""

# not 연산자
# - 단항 연산자
# - 피연자의 값을 반전 : 참 -> 거짓 또는 거짓 -> 참
"""
if not(2 > 3):
    print("T 1")
else :
    print("F 1")

if not(2 < 3):
    print("T 1")
else :
    print("F 2")
"""

# 복합(Compound) 연산자
# - 이항 연산자
# - 지정된 연산 후 대입 실시

"""
value = 1

value += 1

print(value)

value *= 3

print(value)

value /= 3

print(value)

value **= 10

print(value)

value //= 1000

print(value)
"""

# 삼항 연산자 : 조건식을 이용해서 참, 거짓 둘 중 하나 선택
# "'참' 인 경우 선택값" if 조건식 else "'거짓'인 경우 선택 값"
# if else 문과 유사하지만, 한줄로 간략하게 표기할 수 있는 장점이 있음

"""
value = "참 입니다." if 2 > 3 else "거짓 입니다."

print(value)
"""

"""
count = 1

for value in range(1,101) :
    if value == 8 * count :
        print(value)
        count += 1
"""



# 성적을 입력 받는데에 있어서 상식적으로 1~100 사이의 수를 넣어야 하지만
# 그 이외의 수를 받으면 마지막 else 문으로 인해 F 가 나오므로 
# 그 점을 보안 하기 위한 반복문 
# 따라서 1 ~ 100 사이의 수를 입력 받지 않았다면 
# 제대로 된 값을 받기까지 무한루프..

"""
print("성적을 입력하세요.")
InpuRecord = input(" ")

while int(InpuRecord) > 100 or int(InpuRecord) < 1 :
    print("1 ~ 100 사이 정수로 성적을 입력하세요.")
    InpuRecord = input(" ")


if int(InpuRecord) >= 95 :
    print("A+")

elif int(InpuRecord) >= 90 :
    print("A")
    
elif int(InpuRecord) >= 85 :
    print("B+")

elif int(InpuRecord) >= 80 :
    print("B")

elif int(InpuRecord) >= 75 :
    print("C+")

elif int(InpuRecord) >= 70 :
    print("C")

elif int(InpuRecord) >= 65 :
    print("D+")

elif int(InpuRecord) >= 60 :
    print("D")

else :
    print("F")  

"""        



# 흐름제어 란?
"""
print("hello")

print("안녕하세요")

value = False

# value 가 "참" 이면 2단 구구단 출력

if value :
    for value in range(1,10):
        print("2 X ", value, " = ", 2*value)

# value 가 "거짓" 이면 3단 구구단 출력
else :
    iCount = 1
    while iCount <= 9:
        print("3 X ", iCount, " = ", 3*iCount)
        iCount += 1
"""

# 선택 흐름 제어문 : if 문
"""
print("1")

# 조건문이 "참"인 경우만 실행 될 경우
# 단일 if 문 사용
if True :
    print("T 1-1") # "참" 인 경우 실행될 문장이 2라인 이상인 경우
    print("T 1-2") # "참" 인 경우 실행될 문장들의 띄어쓰기를 반드시 일치

print("3")
"""

# 출력 결과> 1  T 1-1   T 1-2   3
# 이유> if 조건문 밖의 출력 명령어는 참 거짓 관계없이 출력이 되지만 
# 참 일 경우에만 출력되는 if 조건문 내의 출력문은 
# 조건을 거짓 으로 바꿧을때 출력되지 않는다

# 키보드로 부터 정수를 입력 받아 입력 갑의 홀수, 짝수를 구분하여, 짝수일 경우만
# "짝수 입니다" 문자열을 화면에 출력하는 프로그램을 작성하여라

"""
InpuValue = int(input("정수를 입력하세요 "))

if InpuValue % 2 == 0 :
    print("짝수 입니다.")
"""

# 선택 흐름 제어문: if ~ else 문

"""

# 키보드로부터 문자열 입력
inputValue = input("정수를 입력하세요 ")
inputValue = int(inputValue) # 문자형 -> 정수형 형 변환

# inputValue 나머지 값이 0일 경우 "짝수"
# 아닐 경우 홀수
if inputValue % 2 == 0 :
    print("짝수 입니다") # 짝수일 경우 화면에 문자열 출력
else :
    print("홀수 입니다") # 짝수가 아니라면 "홀수"
"""

# 키보드로 부터 정수를 입력 받고
# 0 또는 양수이면 "0 또는 양수" 를 문자열로 출력
# 음수 이면 "음수" 문자열을 화면에 출력하는 프로그램을 작성하라
"""

inputValue = int(input("정수를 입력하세요 "))

if inputValue >= 0 :
    print("0 또는 양수입니다")
else :
    print("음수 입니다")
"""

# 선택 흐름 제어문 : if ~ elif 문

# 키보드로부터 정수를 입력 받아
# 아래 성적으로 환산하는 프로그램을 작성하라
# 90 <= 점수       이면 "A"
# 80 <= 점수 < 90  이면 "B"
# 70 <= 점수 < 80  이면 "C"
# 60 <= 점수 < 70  이면 "D"

"""
inputValue = int(input("정수를 입력하세요"))

if inputValue >= 90 :
    print("A")
elif inputValue >= 80 :
    print("B")
elif inputValue >= 70 :
    print("C")
elif inputValue >= 60 :
    print("D")    

print("프로그램 종료")
"""

# 키보드로 부터 정수를 입력 받고
# 0 이면 "0" 을 문자열로 출력
# 양수 이면 "양수" 음수 이면 "음수" 문자열을 출력하는 프로그램 작성
"""
inputValue = int(input("정수를 입력하세요 "))

if inputValue > 0 :
    print("양수")
elif inputValue < 0 :
    print("음수")
elif inputValue == 0 :
    print("0") 
"""

# 선택 흐름 제어문 : if ~ elif ~ else 문

# 키보드로 부터 정수를 입력 받아
# 아래의 성적으로 환산하는 프로그램을 작성하라
# 90 <= 점수       이면 "A"
# 80 <= 점수 < 90  이면 "B"
# 70 <= 점수 < 80  이면 "C"
# 60 <= 점수 < 70  이면 "D"
# 아니면 "F"

"""
inputValue = int(input("정수를 입력하세요 "))

if inputValue >= 90 :
    print("A")
elif inputValue >= 80 :
    print("B")
elif inputValue >= 70 :
    print("C")
elif inputValue >= 60 :
    print("D")    
else :
    print("F")
"""

# 키보드로부터 영문 문자열을 입력 받아, 테이블 규칙을 따라
# 한글로 변환하는 프로그램을 작성하라
# 단 , 테이블 이외의 영문 이름이 입력 될 경우 "그 외" 문자열 출력

"""
inputCname = input("회사명을 입력하세요 ")

if inputCname == "SAMSUNG" :
    print("삼성")

elif inputCname == "NAVER" :
    print("네이버")

elif inputCname == "LG" :
    print("엘쥐")

elif inputCname == "HYUNDAI" :
    print("현대")

elif inputCname == "KAKAO" :
    print("카카오")

elif inputCname == "SK" :
    print("에스케이")

else :
    print("그 외")
"""

# LOOP 반복문
# for , while
# for -> 정해진 횟수의 반복을 실행할 경우에 주로 사용
# while -> for 와 동일 , 하지만 주로 횟수가 정해지지 않은 반복문 작성 시 사용
"""
for value in [1, 2, 3]:
    print(value)

value = 1

while value <= 3 :
    print(value)
    value += 1

"""

# for 변수 in 리스트
# 리스트 내 각 원소 순회 시 실행

# 리스트 [5, 3, 1]의 원소 개수 : 3
# 따라서 아래 For 문은 3번 반복
# 매 반복 시 리스트 원소값 value 변수에 저장
"""
for value in [5, 3, 1]:
    print(value)
"""
# 실행 결과 5, 3, 1

# range()함수
"""
for value in range(2):
    print(value)          # 0, 1

for value in range(3):  
    print(value)          # 0, 1, 2

for value in range(1, 2):
    print(value)          # 1

for value in range(1, 3):
    print(value)          # 1, 2

for value in range(1, 11, 3):
    print(value)          # 1, 4, 7, 10

for value in range(10, 0, -3):
    print(value)          # 10, 7, 4, 1
"""

# 3, 6, 9 게임 구현
"""
for index in range(1, 60) : 
    value = str(index) # 현 숫자(정수)를 문자열로 변환
    flag  = False      # 현 숫자 내 3, 6, 9 숫자가 있는지 나타내는 플래그
    msg   = ""

    # 문자열 개수 만큼 순회
    # 예) "34" -> 2번 순회, 첫번째 "3" 두번째 "4"
    for index_char in value :
        # 현 문자가 3, 6, 9 중 하나 일 경우 "박수" 출력
        if index_char == "3" or index_char == "6" or index_char == "9" :
            msg += "박수 "
            flag = True # 현 숫자 내 3, 6, 9 가 존재 함으로 플래그  ON
    
    if flag : # 3, 6, 9 중에 하나
        print(msg)
    else :    # 3, 6, 9 가 아닐 경우
        print(index)  # 숫자 출력

"""

# for 문 으로 구구단 구현
"""
for timesTable in range(2, 9):
    
    for value in range(1, 10):
        if timesTable % 2 == 0 :
            print(timesTable, " X ", value, " = ", timesTable*value)            
        else :
            pass
"""

# while 문
# 동작 절차 
# while 의 조건식이 "참" 인 동안 while 블록 내 코드 실행
# 일반적으로 반복 횟수가 일정하게 정해지지 않을 경우 사용
"""
flag = True
while flag :
    value = int(input("양의 정수를 입력하세요 "))

    if value > 0:
        print("입력값: ", value)
    else :
        flag = False 
"""
# 메뉴 선택 후 구구단 -> 메뉴를 함수로 지정 후 호출 호출시 함수 뒤 ; 붙임

"""
def menu_print():
    print("-----------------")
    print("1. 2단 구구단 출력")
    print("2. 4단 구구단 출력")
    print("3. 프로그램 종료")
    print("-----------------")

flag = True
while flag :
    menu_print();

    inputValue = int(input("메뉴를 선택 해 주세요 "))

    if inputValue == 1:
        for num in range(1, 10):
            print("2 X ", num, " = ", 2*num)
    elif inputValue == 2:
        num = 1
        while num <= 9:
            print("4 X ", num, " = ", 4*num)
            num += 1
    elif inputValue == 3:
        flag = False
    else:
        print("1~3 사이의 값을 입력해주세요")
"""

# break 문

# 반복문(Loop) 내 사용
# 현 반복문을 탈출하는 용도로 사용

# Loop From 0 to 9
"""
for value in range(10):
    print(value)

    # value 값이 5일 경우
    if value == 5:
        break # Loop문 탈출

print("END")
"""
"""
while True:
    value = int(input("숫자를 입력하세요 "))

    print("입력 값 : ",value)

    if value < 0:
        break

print("END")

"""

# 1~100 사이 정수 중 7의 배수이면서, 11의 배수인 수 중 제일 작은 값을 출력하라
# 7과 11의 최소공배수
"""
for count in range(1,101):
    Seven = 7
    Eleven = 11

    if Seven*Eleven == count :
        print("7과 11의 최소공배수는 : ",count)

"""
"""
for value_1 in range(2):
    for value_2 in range(2):
        for value_3 in range(2):
            if value_2 == 1:
                break

            print("value 1 : ", value_1,
                  "value 2 : ", value_2,
                  "value 3 : ", value_3)
"""

# countinue 문
# 반복문(Loop)내 사용
# countinue 하위 문장을 실행하지 않고, 반복문 조건식 으로 이동
"""
for value in range(1, 6):
    print(value)

    if value == 2:
        continue 

    print("---------")

print("End")

"""

# 구구단 중 3의 배수단 만 출력하는 프로그램을 countinue문을 이용하여 작성하라
"""
for timeTable in range(1,10):
    for count in range(1,10):
        if timeTable % 3 == 0:
            print(timeTable, " X ", count, " = ", timeTable*count)
        else :
            continue
"""

# 다음 프로그램의 실행 결과는? 
"""
count = 0 
while count < 3:
    for value in range(1, 3):
        if count == 1:
            continue

        print("count : ", count, ", value : ", value)
    
    count += 1
"""

# pass 문 
# 선택 or 반복문 내 사용
# 아무것도 실행 되지 않음
"""
for value in range(1,4):
    pass
for value in range(1,4):
    print("1")

if 3 > 2:
    pass
    print("2")

print("3")
"""

# 실습1
# while 문을 사용
"""
count = 1
star = "*"
while count <= 5:
    print(star)
    count += 1
    star += "*"
""" 

