# Maximum absolute difference between sum of two contiguous sub-arrays
def maxArrayLeft(inList):
    #find max so far for every element from the left and store in a new array
    size = len(inList)
    maxSoFar = inList[0]
    sum = [0] * size
    sum[0] = maxSoFar
    currMax = inList[0]
    for i in range(1, size):
        currMax = max(inList[i] + currMax, currMax)
        maxSoFar = max(maxSoFar, currMax)
        sum[i] = maxSoFar
    return sum

def maxArrayRight(inList):
    #find max so far for every element from the right and store in the new array
    size = len(inList)
    maxSoFar = inList[size - 1]
    sum = [0] * size
    sum[size - 1] = maxSoFar
    currMax = inList[size - 1]
    for i in range(size - 1, -1, -1):
        currMax = max(currMax, inList[i] + currMax)
        maxSoFar = max(maxSoFar, currMax)
        sum[i] = maxSoFar
    return sum

def findMaxDiff(inList):
    leftMax = maxArrayLeft(inList)
    rightMax = maxArrayRight(inList)
    #min sum array from left
    negList = [0] * len(inList)
    for i in range(0, len(inList)):
        negList[i] = -inList[i]
    leftMin = maxArrayLeft(negList)
    rightMin = maxArrayRight(negList)
    for i in range(0, len(leftMin)):
        leftMin[i] = -leftMin[i]
    for i in range(0, len(rightMin)):
        rightMin[i] = -rightMin[i]
    #min sum array from right
    result = -100
    for i in range(0, len(inList) - 1):
        absValue = max(abs(leftMax[i] - rightMin[i+1]), abs(leftMin[i] - rightMax[i+1]))
        if absValue > result:
            result = absValue
    return absValue

print findMaxDiff([-2, -3, 4, -1, -2, 1, 5, -3])
