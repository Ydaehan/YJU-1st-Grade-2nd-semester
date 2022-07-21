# 5. 문자열에서 특수문자 개수, 글자수 , 단어수 카운트 프로그램 작성
# 특수문자는 3개 사용 : ! . ,

myList          = "!! hello world, it is awesome day."
count           = 0 # 특수문자 수 카운트
allWord         = 0 # 모든 단어
nCount          = 0 # 특수문자가 아닌 글자
for check in range(len(myList)):
    if myList[check].isalpha():         # 내 리스트의 check 번째 원소가 알파벳일때
        if not myList[check + 1].isalpha() or myList[check] == len(myList)-1:
            allWord += 1
            nCount  += 1
        else:
            nCount  += 1
    elif myList[check] != ( "" or " " ):
        count += 1 # 특수문자 수 카운트
# 특수 문자 수
print("특수문자 수 : ",count)
# 단어 수
print("단어 수 : ",allWord)
# 특수 문자 제외 글자 수
print("특수문자 제외 글자 수 : ",nCount)