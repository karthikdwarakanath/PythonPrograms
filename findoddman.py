def oddman(arrayNum):
    tmpArr = []
    for count in range(0, max(arrayNum)):
        tmpArr.append(0)
    for i in range(0, len(arrayNum)):
        if tmpArr[arrayNum[i]-1] == 0:
            tmpArr[arrayNum[i]-1] = 1
        else:
            tmpArr[arrayNum[i]-1] = 0

    for i in range(0, len(tmpArr)):
        if tmpArr[i] == 1:
            return i+1

def oddman2(arrayNum):
    sum = 0
    hashDict = {}
    for i in arrayNum:
        if i in hashDict:
            sum -= i
        else:
            hashDict[i] = 0
            sum += i
    return sum

print oddman2([1, 2, 3, 1, 2])
