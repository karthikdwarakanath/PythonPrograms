def isUnique(str):
    newStr = ''
    for i in range(0, len(str)):
        if str[i] in str[0:i]:
            return False
    return True

print isUnique('asdasdasdasog')
print isUnique('s')
print isUnique('sdf')
