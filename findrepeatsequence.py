# Repeated subsequence of length 2 or more
# Given a string, find if there is any subsequence of length 2 or more that
# repeats itself such that the two subsequence don’t have same character at
# same position, i.e., any 0’th or 1st character in the two subsequences
#  shouldn’t have the same index in the original string.

#Example ABCABD : repeated subsequence of AB

def findrep(inpStr):
    resultStr = ''
    i = 0
    n = len(inpStr)
    while i < n:
        
