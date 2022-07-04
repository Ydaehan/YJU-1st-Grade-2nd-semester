# while 문을 사용하여 1~1000까지의 자연수 중 3 의 배수 합 구하기

# 출력결과: 1~1000 사이 정수 중 3의 배수 합은 : 166833
"""
value = 1 
total = 0
while value <= 1000:
    if value % 3 == 0:
        total += value
        value += 1
    elif value == 1000:
        print("1~1000 사이 정수 중 3의 배수 합은 : ", total)
        break
    else :
        value += 1
        continue
"""

# for 문을 사용하여 문자열 내 'h'의 개수를 출력하는 프로그램을 작성하라

"""
myString = "hello hyundai hoho"
count = 0
for i in myString:
    if i == "h":
        count += 1
        
print("문자열 내 h 갯수 : ",total)
"""

# for 문을 사용하여 문자열 내 단어 개수를 출력하는 프로그램을 작성하라

"""
myString = "It is a great weather with you"
count = 1

for a in myString :
    if a == " ":
        count += 1

print("문자열 단어 갯수 : ", count)
"""

# for 문을 사용하여 아래 학생들의 성적에 대한 총합, 평균, 학생 수를 출력하는 프로그램을 작성하라
"""
score = [99, 29, 30, 40, 20, 60]

student_num = 0
sum = 0
avg = 0

for i in score:
    sum += i
    student_num += 1

avg = sum / student_num

print("학생 수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)
"""

# 메뉴 출력후 번호를 입력 받아 괴목 선택
# 선택받은 과목의 점수 입력
# 선택 된 과목의 점수 출력
# 모든 과목 선택하여 모두 기입 가능
# 따로 입력 시 마지막에 모든 과목 점수 표기 실패
"""

count = 1
inputScoreKo = 0
inputScoreMa = 0
inputScoreSo = 0
inputScoreSi = 0
inputScoreEn = 0
inputScoreFo = 0


def All_Subject():
    print("국어")
    inputScoreKo = int(input("점수를 입력하세요 : "))
    print("수학")
    inputScoreMa = int(input("점수를 입력하세요 : "))
    print("사회")
    inputScoreSo = int(input("점수를 입력하세요 : "))
    print("과학")
    inputScoreSi = int(input("점수를 입력하세요 : "))
    print("영어")
    inputScoreEn = int(input("점수를 입력하세요 : "))
    print("외국어")
    inputScoreFo = int(input("점수를 입력하세요 : "))
    
    print("국어 :",inputScoreKo)
    print("수학 :",inputScoreMa)
    print("사회 :",inputScoreSo)
    print("과학 :",inputScoreSi)
    print("영어 :",inputScoreEn)
    print("외국어 :",inputScoreFo)

def End_input():
    print("그만 입력 하시겠습니까?")
    print("입력을 중단하면 남은 과목은 0점 표기 됩니다")
    print(" Y / N ")
    inputAnswer = input(" ")
    if inputAnswer == "Y":
        count += 1
        print("국어 :",inputScoreKo)
        print("수학 :",inputScoreMa)
        print("사회 :",inputScoreSo)
        print("과학 :",inputScoreSi)
        print("영어 :",inputScoreEn)
        print("외국어 :",inputScoreFo)
        
    if inputAnswer == "N":
        pass
    

def TotalSubjectScore_Menu() :
    print("1. 국어")
    print("2. 수학")
    print("3. 사회")
    print("4. 과학")
    print("5. 영어")
    print("6. 외국어")
    print("7. 모두 입력")
    
    selectSubject = int(input("점수를 기입 할 과목을 선택하세요 : "))
    if selectSubject == 1 :
        print("국어를 선택 했습니다")
        inputScoreKo = int(input("점수를 입력하세요 : "))
        print("국어 :",inputScoreKo)
        End_input()
        
    elif selectSubject == 2 :
        print("수학을 선택 했습니다")
        inputScoreMa = int(input("점수를 입력하세요 : "))
        print("수학 :",inputScoreMa)
        End_input()
        
    elif selectSubject == 3 :
        print("사회를 선택 했습니다")
        inputScoreSo = int(input("점수를 입력하세요 : "))
        print("사회 :",inputScoreSo)
        End_input()
        
    elif selectSubject == 4 :
        print("과학을 선택 했습니다")
        inputScoreSi = int(input("점수를 입력하세요 : "))
        print("과학 :",inputScoreSi)
        End_input()
        
    elif selectSubject == 5 :
        print("영어를 선택 했습니다")
        inputScoreEn = int(input("점수를 입력하세요 : "))
        print("영어 :",inputScoreEn)
        End_input()
        
    elif selectSubject == 6 :
        print("외국어를 선택 했습니다")
        inputScoreFo = int(input("점수를 입력하세요 : "))
        print("외국어 :",inputScoreFo)
        End_input()
        
    elif selectSubject == 7 :
        print("모두 입력을 선택 했습니다")
        All_Subject()
        count += 1
    else : 
        print("잘못된 입력 입니다")
        




while count == 1 :
    TotalSubjectScore_Menu()
"""
# for 문을 이용하여 별 1~ 5개 출력
"""
star = "*"
for i in range(1,6):
    print(star)
    star += "*"
"""

"""    
# while 문을 이용하여 별 1~ 5개 출력 
a = 1
star = "*"
while a <= 5:
    print(star)
    a += 1
    star += "*"
"""

# 1~ 1000 까지 수 2의 배수 4의 배수 의 각각의 합을 구하고 2와 4의 최대 공약수와 최소 공배수

"""
Total_T = 0 
Total_F = 0
value_a = 0
value_b = 0
for num in range(1,1001):
    if num % 2 == 0 :
        Total_T += num

for num in range(1,1001):
    if num % 4 == 0 :
        Total_F += num

for num in range(1,1001):
    if (num % 2 == 0) and (num % 4 == 0):
        value_a = num
        break

a = 2
b = 4

for num in range(min(a,b),0,-1):
    if (a % num == 0) and (b % num == 0):
        value_b = num
        break

print("2의 배수 합 : ",Total_T,"4의 배수 합 : ",Total_F)
print("2와 4의 최소공배수 : ",value_a)
print("2와 4의 최대공약수 : ",value_b)
"""

#피라미드 만들기
"""
inputNum = int(input("피라미드의 층을 입력해주세요 : "))
i = 1
while i <= inputNum:
    print(" "*(inputNum-i),"*"*(2*i-1))
    i += 1
"""