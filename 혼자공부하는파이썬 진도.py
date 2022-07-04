# 108p 불 자료형과 if 조건문

# Boolean => 불린 or 불리언  프로그래밍에서는 짧게 Bool
# 한국에서는 Boolean Algebra => 불 대수
# Boolean Operator -> 불 연산자
"""
print(True) # 파이썬에서는 True and False 첫 글자를 대문자로 적어야함
print(False)
"""

# 불 만들기: 비교 연산자
# == 같다 != 다르다
# < 작다 > 크다
# <= 작거나 같다 >= 크거나 같다

"""
print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)
"""

# 문자열도 가능
"""
print("가방" == "가방")
print("가방" != "하마")
print("가방" < "하마") # 사전 순서로 가방이 하마보다 앞에 있기때문에 
print("가방" > "하마") # 가방이 하마보다적은 수를 가지고 있다
"""
# 불 연산하기 : 논리 연산자

# not => 아니다 => 불을 반대로 전환
# and => 그리고 => 피 연산자 두개가 모두 참일때 True 출력 그외 모두 False
# or => 또는 => 피 연산자 두 개중 하나만 참이여도 True 출력 모두 거짓이면 False 출력

# 단항 연산자
#피 연산자 가 한 개

# 이항 연산자
#피 연산자 가 두 개

# not 연산자 -> 단항 연산자
"""
print(not True)
print(not False)
"""
"""
x = 10 
under_20 = x < 20
print("under_20:", under_20)
print("Not under_20:", not under_20)
"""


# if 조건문
# if 조건문 뒤에는 반드시 :

"""
# 입력을 받음
number = input("정수 입력> ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수 입니다")
    
# 음수 조건
if number < 0:
    print("음수 입니다")
    
# 0 조건
if number == 0:
    print("0 입니다")
"""

# 날짜 . 시간 출력
"""
# 날짜 / 시간 관련 기능 추가
import datetime

# 현재 날짜 / 시간 구하기
now = datetime.datetime.now()

# 출력
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
"""
"""
# 날짜 / 시간 관련 기능 추가
import datetime

# 현재 날짜 / 시간 구하기
now = datetime.datetime.now()

# 출력
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))
"""
"""
# 날짜 / 시간 관련 기능 추가
import datetime

# 현재 날짜 / 시간 구하기
now = datetime.datetime.now()

# 오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
    
# 오후 구분
if now.hour >= 12:
    print("현재 시각은 {}로 오후입니다!".format(now.hour))
"""

# 119p
"""
# 날짜 / 시간 관련 기능 추가
import datetime

# 현재 날짜 / 시간 구하기
now = datetime.datetime.now()

# 봄
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
    
# 여름
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))
# 가을
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))
# 겨울
if 12 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
"""

# 121p

"""
# 입력 받음
number = input("정수 입력> ")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수 입니다")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수 입니다")
"""

# 122p

"""
# 입력을 받습니다.
number = input("정수 입력> ")
last_charcter = number[-1]

# 짝수 조건
if last_charcter in "02468":  # in 연산자는 뒤에 오는 문자열이 앞의 변수내에 존재하는지 확인
    print("짝수 입니다")
    
if last_charcter in "13579":  # 확인이 되었다면 출력
    print("홀수 입니다")
"""

# p123 
"""
# 입력을 받습니다.
number=input("정수 입력> ")
number=int(number)

# 짝수 조건
if number%2==0:
    print("짝수 입니다")

if number%2!=0:
    print("홀수 입니다")
"""

# p126

# if ~ else 와 elif
# 시행 해봄
# p128
"""
import datetime

now = datetime.datetime.now()
month = now.month

if 3<=month<=5:
    print("봄")
elif 6<=month<=8:
    print("여름")
elif 9<=month<=11:
    print("가을")
else:
    print("겨울")
"""

# p132

# False 로 변환되는값
"""
print("# if 조건문에 0 넣기")
if 0:
    print("True")
else:
    print("False")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("True")
else:
    print("False")
"""

# p135
"""
number = int(input("정수: "))

# if
if number > 0:
    # 양수 일 때 : 아직 미구현 상태 입니다.
    raise NotImplementedError
else:
    # 음수 일 때 : 아직 미구현 상태 입니다.
    raise NotImplementedError
"""

# p140

# 리스트 와 반복문
# 리스트 연산자 : 연결(+) 반복(*) len()

# 리스트를 선언
"""
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# list")
print("list_a =",list_a)
print("list_b =",list_b)
print()

# 기본연산자
print("# 리스트 기본 연산자")
print("list_a + list_b =",list_a + list_b)
print("list_a * 3 = ",list_a*3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) =",len(list_a))
"""

# 리시트에 요소 추가하기: append, insert
"""
# 리스트를 선언합니다.
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)
# 한번에 여러 요소를 추가할 때 에는 extend( )함수 사용
"""
