# Enter your code here. Read input from STDIN. Print output to STDOUT
# Spiral Matrix - In a loop, should print and remove the first row
#                          , should print and remove the last column
#                          , should print and remove the inverted last row
#                          , should print and remove the inverted first column
# Do the above until the matrix is empty
def printSpiral(intMatrix):
    #main list to be printed after matrix is emptied
    printList = []
    if not intMatrix:
        print 'Input Error'
        return
    while len(intMatrix) > 0:
        firstRow, lastCol, lastRow, firstCol = [], [], [], []
        intMatrix, firstRow = getFirstRow(intMatrix)
        intMatrix = cleanMatrix(intMatrix)
        if len(intMatrix) > 0:
            intMatrix, lastCol = getLastCol(intMatrix)
            intMatrix = cleanMatrix(intMatrix)
        if len(intMatrix) > 0:
            intMatrix, lastRow = getInvLastRow(intMatrix)
            intMatrix = cleanMatrix(intMatrix)
        if len(intMatrix) > 0:
            intMatrix, firstCol = getInvFirstCol(intMatrix)
            intMatrix = cleanMatrix(intMatrix)
        # append the firstrow, lastcolumn, lastrow and firstcol
        # to the main printlist
        if len(firstRow) > 0:
            for i in firstRow:
                printList.append(i)
        if len(lastCol) > 0:
            for i in lastCol:
                printList.append(i)
        if len(lastRow) > 0:
            for i in lastRow:
                printList.append(i)
        if len(firstCol) > 0:
            for i in firstCol:
                printList.append(i)
    #print the overall spiral sequence
    print ",".join(printList)
    return

def cleanMatrix(intMatrix):
    #helper function to clean out empty lists
    for i in intMatrix:
        if len(i) == 0:
            intMatrix.remove(i)
    return intMatrix

def getFirstRow(intMatrix):
    #helper function to get the first row of spiral
    firstRow = intMatrix[0]
    del intMatrix[0]
    return intMatrix, firstRow

def getLastCol(intMatrix):
    #helper function to get the last column of spiral
    lastCol = []
    for i in range(0, len(intMatrix)):
        lastCol.append(intMatrix[i][-1])
        del intMatrix[i][-1]
    return intMatrix, lastCol

def getInvLastRow(intMatrix):
    #helper function to get the inverted last row of spiral
    lastRow = intMatrix[-1]
    del intMatrix[-1]
    return intMatrix, lastRow[::-1]


def getInvFirstCol(intMatrix):
    #helper function to get the inverted first column of spiral
    firstCol = []
    for i in range(0, len(intMatrix)):
        firstCol.append(intMatrix[i][0])
        del intMatrix[i][0]
    return intMatrix, firstCol[::-1]

def getSpiral():
    #Input method: Gets the row and columns
    #Runs a loop for the number of rows and gets input for every row
    #Creates a matrix using list of lists
    #return matrix if input is correct
    r, c = raw_input().split(',')
    r, c = int(r), int(c)
    if r < 1 or c < 1:
        print 'Row and columns to be positive integers only'
        return None
    intMatrix = []
    for i in range(0, r):
        intMatrix.append(raw_input().split(','))
        if len(intMatrix[i]) < c:
            print "Matrix incomplete"
            return None
    return intMatrix

iMatrix = getSpiral()
printSpiral(iMatrix)

#Testcases:
#test 1:
# 1,4
# 1,2,3,4
#output = 1,2,3,4
#test 2:
# 4,1
# 1
# 2
# 3
# 4
#output = 1,2,3,4
