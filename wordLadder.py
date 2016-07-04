#rds (start and end), and a dictionary, find the length of shortest
#  transformation sequence from start to end, such that only one letter can be
#  changed at a time and each intermediate word must exist in the dictionary.
#   For example, given:
# #
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# the program should return its length 5.

from collections import deque
class WordNode(object):
    def __init__(self, word, numSteps):
        self.word = word
        self.numSteps = numSteps

def findLengthOfTransformation(start, end, wordDict):
    bfsQ = deque()
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
    'q','r','s','t','u','v','w','x','y','z']
    startWord = WordNode(start, 0)
    bfsQ.append(startWord)
    while len(bfsQ) > 0:
        top = bfsQ.popleft()
        if top.word == end:
            return top.numSteps
        for i in range(0, len(top.word)):
            for c in alpha:
                tmp = top.word
                if c != top.word[i]:
                    str1 = top.word[:i] + c + top.word[i+1:]
                if str1 in wordDict:
                    newWord = WordNode(str1, top.numSteps+1)
                    bfsQ.append(newWord)
                    del wordDict[str1]
                top.word = tmp

print findLengthOfTransformation('hit', 'cog', {'hot':1, 'dot':1, 'dog':1, 'cog':1})
