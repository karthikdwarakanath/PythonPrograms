# Given an sorted array of positive integers, count number of occurrences for
# each element in the array. Assume all elements in the array are less than some
# constant M (much smaller than n).
# Do this without traversing the complete array. i.e. expected time complexity is less than O(n).

# Examples - n = 7, m = 4,  [1,2,3,3,3,1,1,2]

def positiveIntFreq(inputArr, m):
    resultArr = [0] * (m + 1)
    resultArr = findFreq(inputArr, 0, len(inputArr) - 1, resultArr)
    for i, j in enumerate(resultArr):
        print i, j
    return

def findFreq(inputArr, start, end, resultArr):
    if inputArr[start] == inputArr[end]:
        resultArr[inputArr[start]] += end - start + 1
    else:
        mid = start/2 + end/2
        findFreq(inputArr, start, mid, resultArr)
        findFreq(inputArr, mid+1, end, resultArr)
    return resultArr

print positiveIntFreq([1,1,1,2,3,3,3,3,4,4,4], 5)
print positiveIntFreq([1,2,3,4,5], 6)
