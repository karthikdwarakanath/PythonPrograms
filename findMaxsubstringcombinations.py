def findSum(numList):
    sum = 0
    listLen = len(numList)
    if listLen == 1:
        return 1
    if (numList[listLen-2] * 10 + numList[listLen-1]) > 26:
        sum += findSum(numList[:-1])
    else:
        sum += findSum(numList[:-1]) + 1
    return sum

numList=[1,2,2,2,2,1,3,6]
print findSum(numList)
