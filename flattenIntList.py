def flattenList(inputList):
    out = []
    for numList in inputList:
        if isinstance(numList, (list or tuple)):
            out = out + flattenList(numList)
        else:
            out.append(numList)
    return out

a = [1,2,3]
b = [1,[2,3],4]
c = [[1,2,3,4],[5,[6,7,[8,9]]]]
print flattenList(a)
print flattenList(c)
