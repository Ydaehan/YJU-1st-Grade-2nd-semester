# 줄 수 입력
lineNum = int(input("줄 수를 입력 하세요. "))
# 문자열 입력 , 줄 수 만큼
textLine = []
for index in range(lineNum):
    textLine.append(input(str(index + 1) + "번째 문장을 입력하세요. "))
while True:
    # 검색어 입력
    findWord = input("검색할 문자열을 입력하세요. ")
    # 검색 결과 출력
    # 문자 순회
    allWord         = 0
    matchCount      = 0
    matchLine       = []
    for row in range(lineNum):
        index = 0
        previousWord = ""   # 이전 문자
        nextWord = ""       # 다음 문자
        noMatchCount    = 0
        for col in range(len(textLine[row])):
            if col == (len(textLine[row]) - 1) :
                nextWord = ""
            else :
                nextWord = textLine[row][col + 1]   # 다음 문자 가져오기
            # 매칭 시작
            if index == 0 and textLine[row][col] == findWord[index]:
                if not previousWord.isalpha():
                    index += 1
                    if not nextWord.isalpha():
                        allWord += 1
            # 매칭 계속 elif 로 index 가 0 이 아닐때 작동
            elif textLine[row][col] == findWord[index]:
                # 매칭 종료
                if index == (len(findWord) - 1) and not nextWord.isalpha():
                    if noMatchCount == 0 :
                        matchCount += 1
                        if row + 1 not in matchLine :
                            matchLine.append(row + 1)
                        index = 0
                    else :
                        allWord += 1
                        noMatchCount = 0
                # 매칭 계속
                else :
                    if index == (len(findWord) - 1) :
                        noMatchCount += 1
                        continue
                    elif not nextWord.isalpha():
                        allWord += 1
                        continue
                    index += 1
            # 문자열이 일치하지 않을 경우 리셋
            else : 
                index = 0
                if textLine[row][col] != ("" or " "):
                    noMatchCount += 1
                    if not nextWord.isalpha():
                        allWord += 1
                        noMatchCount = 0
            previousWord == textLine[row][col] # 이전 문자 가져오기
    if matchCount == 0:
        print("일치하는 단어가 없습니다.")
        continue
    print(findWord,"를 찾았습니다.")
    print("일치한 줄 수 : ",matchLine)
    print("일치한 갯수  : ",matchCount)
    print("총 단어 수   : ",allWord + matchCount)
