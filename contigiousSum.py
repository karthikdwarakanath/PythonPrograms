# Given an array of positive integers and a target total of X,
# find if there exists a contiguous subarray with sum = X
#
# [1, 3, 5, 18] X = 8 Output: True
# X = 9 Output: True
# X = 10 Output: False
# X = 40 Output :False
#

from collections import deque

def findContigious(inList, target):
    if len(inList) == 0:
        return False
    if len(inList) == 1:
        return (inList[0] == target)
    sum = 0
    resultQ = deque()
    for i in inList:
        if i <= target:
            while sum+i > target:
                tmp = resultQ.popleft()
                sum -= tmp
            resultQ.append(i)
            sum += i
            if sum == target:
                return True
        else:
            resultQ.clear()
            sum = 0
    return False

print findContigious([1,3,5,18], 8)
print findContigious([1,3,5,18], 9)
print findContigious([1,3,5,18], 10)
print findContigious([1,3,5,18], 40)
