# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
#while preserving the order of characters. No two characters may map to the
#same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    morphDict = {}
    str1 = list(s)
    str2 = list(t)
    if not str1 or not str2:
        return False
    if len(str1) != len(str2):
        return False
    for i in range(0, len(str1)):
        if str1[i] in morphDict:
            if morphDict[str1[i]] != str2[i]:
                return False
        else:
            morphDict[str1[i]] = str2[i]
    return True

print isIsomorphic('egg', 'add')
print isIsomorphic('foo', 'bar')
