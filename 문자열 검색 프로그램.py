# 흐름제어 와 리스트인덱스 사용 함수사용x

print("입력 문자열의 줄(Line) 수를 입력하세요!")
inputLine = int(input())

strLinelist = [] # 문장 별 로 리스트 분리
# 단어 수
wordNum = 0
myStr = ""
for lineNum in range(inputLine):
    strList = []
    # 영문 문자열을 키보드로부터 입력받아 리스트에 저장
    print(lineNum + 1,"번째 라인의 문자열을 입력하세요.")
    inputStr = input()
    index = 0               # 단어의 인덱스 판단 라인마다 초기화
    for word in inputStr:
        if word != " ":
            myStr += word                                # 띄워 쓰기 가 아닐때만 문자열 저장
        # myStr 이 공백이 아니면서 
        # 띄워 쓰기 or 문자열의 마지막일때 단어 판단 리스트 저장
        if myStr != "" and (word == " " or index == len(inputStr) - 1): 
            strList.append(myStr)
            wordNum += 1                  # 단어 갯수 카운트
            myStr = ""                    # 단어 판별 끝 초기화
        index += 1                        # 반복 할때 마다 인덱스 값  + 1
    strLinelist.append(strList)
# 검색 단어를 키보드로부터 다시 입력 받아 해당
# 단어가 있을 경우 결과 값 출력

while True :
    # 검색 된 횟수
    count = 0
    # 검색 된 라인 수
    lineNumList = []
    lineCount = 1
    print("검색 할 문자열을 입력하세요.")
    inputSearch = input()
    for lineList in strLinelist:    # 줄 수 별로 나눈 리스트를 원소 한개씩 들고와서
        for word in lineList:       # 들고 온 원소(리스트)를 다시 하나씩 가져와서 단어로 비교
            if inputSearch == word :
                count += 1      # 검색 문자가 있다면 + 1
                if lineCount not in lineNumList : # 한 라인에 검색문자가 2개 이상 있다면 1번만 리스트에 저장
                    lineNumList.append(lineCount)
        lineCount += 1          # 마지막에 줄 수 + 1
    if count >= 1 :
        print()
        print(inputSearch,"를 찾았습니다.")
        print("검색된 라인 수",lineNumList)
        print("검색된 횟수 :",count)
        print("총 단어 수 :",wordNum)
    else :
        print()
        print("찾을 수가 없습니다.",end="")