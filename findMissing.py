# Find lost element from a duplicated array
# Given two arrays which are duplicates of each other except one element,
# that is one element from one of the array is missing, we need find that missing element.
#
# Examples:
#
# Input:  arr1[] = {1, 4, 5, 7, 9}
#         arr2[] = {4, 5, 7, 9}
# Output: 1
# 1 is missing from second array.
#
# Input: arr1[] = {2, 3, 4, 5}
#        arr2[] = {2, 3, 4, 5, 6}
# Output: 6
# 6 is missing from first array.
def findMissing(arr1, arr2):
    sum1 = 0
    sum2 = 0
    for i in arr1:
        sum1 += i
    for i in arr2:
        sum2 += i
    if sum2 > sum1:
        return sum2 - sum1
    else:
        return sum1 - sum2

print findMissing([1,4,5,7,9], [4,5,7,9])
print findMissing([2,3,4,5],[2,3,4,5,6])
