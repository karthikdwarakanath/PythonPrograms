# Minimum sum of two numbers formed from digits of an array
# Given an array of digits (values are from 0 to 9), find the minimum possible
# sum of two numbers formed from digits of the array. All digits of given array
#  must be used to form the two numbers.

def findMinSum(inputList):
    inList = sorted(inputList)
    a = ''
    b = ''
    i = 0
    while i < len(inList) - 1:
        a += str(inList[i])
        b += str(inList[i+1])
        i += 2
    if len(inList) % 2 != 0:
        a += str(inList[len(inList) - 1])
    return int(a) + int(b)

print findMinSum([6, 8, 4, 5, 2, 3])
print findMinSum([5, 3, 0, 7, 4])
