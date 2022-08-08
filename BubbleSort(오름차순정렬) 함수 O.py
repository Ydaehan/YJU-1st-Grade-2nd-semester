# N개의 정수를 입력 받아 리스트 저장 함수
def getInputValue(argN):
    tempInputValueList = []
    for a in range(argN):
        inputValue = int(input(str(a + 1) + "번째 정수를 입력하세요 : "))
        tempInputValueList.append(inputValue)
    return tempInputValueList

# 리스트 오름차순 정렬 함수
"""
def bubbleSort(argList):
    for iCount in range(len(argList) - 1):
        for jCount in range(len(argList) - iCount - 1):
            if argList[jCount] > argList[jCount + 1]:
                temp = argList[jCount + 1]
                argList[jCount + 1] = argList[jCount]
                argList[jCount] = temp
    return argList
"""
def bubbleSort(argList,asscend = True):
    for iCount in range(len(argList) - 1):
        for jCount in range(len(argList) - iCount - 1):
            comparisonResult = \
                argList[jCount] > argList[jCount + 1] if asscend else argList[jCount] < argList[jCount + 1]
            
            if comparisonResult:
                temp = argList[jCount + 1]
                argList[jCount + 1] = argList[jCount]
                argList[jCount] = temp
inputValueList = getInputValue(5)
bubbleSort(inputValueList)
print(inputValueList)