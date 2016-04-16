def reversStr(str):
    return str[::-1]
#The above solution is simple, clean and uses python features of stepping
#Not sure how efficient python works on this.
#My hunch is that it is pretty quick
print reversStr('kjhsdf')
print reversStr('aba')
print reversStr('skweksowksowks')


def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return True
    countArr = {}
    for i in range(0, len(str1)):
        if str1[i] not in countArr:
            countArr[str1[i]] = 1
        else:
            countArr[str1[i]] += 1
    for i in range(0, len(str2)):
        if str2[i] not in countArr:
            return False
        countArr[str2[i]] -= 1
    for i in countArr:
        if countArr[i] != 0:
            return False
    return True
#The above solution does one pass each of str1 and str2
#And one pass of the count dictionary.
#creates 1 dictionary in total
#space saving solution
#not the most efficient i think

print isPermutation('abc','cba')
print isPermutation('abc','abc')
print isPermutation('abcd','cba')
print isPermutation('abc','csda')
print isPermutation('abc','bcad')
