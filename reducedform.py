# Convert an array to reduced form
# Given an array with n distinct elements, convert the given array to a form
# where all elements are in range from 0 to n-1. The order of elements is same
#, i.e., 0 is placed in place of smallest element, 1 is placed
# for second smallest element, n-1 is placed for largest element.
# Input:  arr[] = {10, 40, 20}
# Output: arr[] = {0, 2, 1}
#
# Input:  arr[] = {5, 10, 40, 30, 20}
# Output: arr[] = {0, 1, 4, 3, 2}

def reducedForm(inArr):
    sortArr = sorted(inArr)
    #sort the input array
    outArr = dict()
    #create a dict of array items and its position
    for i in range(0, len(inArr)):
        outArr[sortArr[i]] = i
    finalArr = []
    #create a final array by running through the input array and looking
    #up the position in the dictionary
    for i in inArr:
        finalArr.append(outArr[i])
    return finalArr

print reducedForm([10, 40, 20])
print reducedForm([5, 10, 40, 30, 20])
