#rotate array of integers by k elements to the right
#[1,2,3,4,5,6], k = 2, -> [5,6,1,2,3,4]

def rotateIntArrByK(inList, k):
    #reverse elements from 0 to n-k
    #reverse elements from k+1 to n
    #reverse the whole array
    n = len(inList)
    i = 0
    j = n-k-1
    while i < j:
        tmp = inList[i]
        inList[i] = inList[j]
        inList[j] = tmp
        i+=1
        j-=1
    i = n-k
    j = n-1
    while i < j:
        tmp = inList[i]
        inList[i] = inList[j]
        inList[j] = tmp
        i+=1
        j-=1
    i = 0
    j = n-1
    while i < j:
        tmp = inList[i]
        inList[i] = inList[j]
        inList[j] = tmp
        i+=1
        j-=1
    return inList

print rotateIntArrByK([1,2,3,4,5,6], 2)
