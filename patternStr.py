# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattList = list(pattern)
        strList = str.split(' ')
        if len(pattList) != len(strList):
            return False
        lookDict = {}
        for item in range(0, len(pattList)):
            if pattList[item] not in lookDict:
                if item == 0:
                    lookDict[pattList[item]] = strList[item]
                elif strList[item] in lookDict.values():
                    return False
                else:
                    lookDict[pattList[item]] = strList[item]
            else:
                if strList[item] != lookDict[pattList[item]]:
                    return False
        return True
