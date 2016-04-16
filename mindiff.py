# Given an unsorted array, find the minimum difference between any pair in given array.
#
# Examples :
#
# Input  : {1, 5, 3, 19, 18, 25};
# Output : 1
# Minimum difference is between 18 and 19
#
# Input  : {30, 5, 20, 9};
# Output : 4
# Minimum difference is between 5 and 9
#
# Input  : {1, 19, -4, 31, 38, 25, 100};
# Output : 5
# Minimum difference is between 1 and -4
def minDiff(intArr):
    #sorted inbuilt function in python
    #complexity is O(nlogn)
    sortArr = sorted(intArr)
    #once sorted, complexity is O(n)
    min = sortArr[1] - sortArr[0]
    for i in range(1, len(sortArr) - 1):
        if (sortArr[i+1] - sortArr[i]) < min:
            min = sortArr[i+1] - sortArr[i]
    return min

print minDiff([1, 5, 3, 19, 18, 25])
print minDiff([30, 5, 20, 9])
print minDiff([1, 19, -4, 31, 38, 25, 100])
