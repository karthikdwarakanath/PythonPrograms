class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        strList = list(s)
        vowels = 'aieou'
        i, j = 0, len(s) - 1
        while i < j:
            if strList[i].lower() not in vowels:
                i += 1
            else if strList[j].lower() not in vowels:
                j -= 1
            else:
                str[i], str[j] = str[j], str[i]
                i += 1
                j -= 1
        return "".join(strList)
