#should return the nth look and say string sequence
def lookandsay(n):
    start = "1"
    for i in range(1, n):
        start = buildLAS(start)
    return start

def buildLAS(inputString):
    resultString = ''
    i = 0
    while i < len(inputString):
        count = 1
        while (i+1 < len(inputString)) and (inputString[i] == inputString[i+1]):
            i += 1
            count += 1
        resultString += str(count) + inputString[i]
        i+=1
    return resultString

print lookandsay(1)
print lookandsay(2)
print lookandsay(3)
print lookandsay(4)
print lookandsay(5)
print lookandsay(6)
