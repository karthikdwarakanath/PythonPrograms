# Palindrome Pairs
# "bob", "gig", "abba"
# Non-examples: "firetruck"
# ["gab", "cat", "bag", "alpha"] => [["gab", "bag"], ["bag", "gab"]]
# gabbag
# baggab
#    ["gab", "cat", "bag", "alpha", "nurses", "race", "car", "run"] => [["gab", "bag"], ["bag", "gab"], ["race", "car"], ["nurses", "run"]]

# ['car', 'car', 'rat', 'tar', 'a', 'a']

def isPalindrome(inputString):
    reverseString = inputString[::-1]
    if reverseString == inputString:
        return True
    else:
        return False

#if it is a substring, the remaining part of the word should also be a palindrome
#one case, where reverse(word) is equal to a given word
#second case, where each word is a substring
#substring can be prefix/post, but remaining part in itself should be a palindrome

def getPalindromePairs(inputList):
    mapOfStrs = {}
    pairList = []
    #creating a map of reverse of the word
    for i in range(0, len(inputList)):
        if inputList[i] not in mapOfStrs:
            mapOfStrs[inputList[i][::-1]] = i
    #Go through the list,
    #get the prefixes and postfixes and check for palindrome
    for word in inputList:
        for char in range(0, len(word)):
            prefix = word[0: char]
            postfix = word[char:]
            if (prefix in mapOfStrs) and isPalindrome(postfix):
                if len(prefix) > 1 or (prefix != word):
                    palindromeStr = word + prefix[::-1]
                    pairList.append([word, prefix[::-1]])
        for char in range(0, len(word)):
            postfix = word[char:]
            prefix = word[:char]
            if (postfix in mapOfStrs) and isPalindrome(prefix):
                if len(postfix) > 1 or (postfix != word):
                    palindromeStr = postfix[::-1] + word
                    pairList.append([postfix[::-1], word])
    return pairList


def isSubString(mainStr, subStr):
    if subStr in mainStr:
        return True
    return False

print getPalindromePairs(["gab", "cat", "bag", "alpha", "nurses", "race", "car", "run"])
print getPalindromePairs(["gab", "cat", "bag", "alpha"])
print getPalindromePairs(["gab", 'bbb', 'bbb'])
print getPalindromePairs(["gab", "cat", "bag", "alpha", "nurses", "race", "car", "run", "abcd", "dcb"])

# print isPalindrome('bob')
# print isPalindrome('boa')
# print isPalindrome('baggab')
# print isPalindrome('b')


# def say_hello():
#     print 'Hello, World'
#     print 'hello again'

# for i in xrange(5):
#     say_hello()
