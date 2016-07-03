# Given an input string, reverse the string word by word.
#  A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces and the words
# are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

def reverseString(inputStr):
    resultStr = ''
    n = len(inputStr)
    i = n-1
    while i >= 0:
        if inputStr[i] != ' ':
            i -= 1
        else:
            resultStr += inputStr[i+1:n]
            resultStr += ' '
            n = i
            i -= 1
    resultStr += inputStr[0:n]
    return resultStr

print reverseString('the sky is blue')
