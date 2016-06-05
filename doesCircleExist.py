def  doesCircleExist(commands):
    x, y = 0, 0
    currDir = 0
    print x, y, currDir
    x, y, currDir = doesCircleExistHelper(commands, x, y, currDir)
    print x, y, currDir
    x1, y1, currDir = doesCircleExistHelper(commands, x, y, currDir)
    print x1, y1, currDir
    x2, y2, currDir = doesCircleExistHelper(commands, x1, y1, currDir)
    print x2, y2, currDir
    x3, y3, currDir = doesCircleExistHelper(commands, x2, y2, currDir)
    print x3, y3, currDir
    if currDir == 0 and x3 == 0 and y3 == 0:
        return 'YES'
    else:
        return 'NO'

def doesCircleExistHelper(commands, x, y, currDir):
    direction = {'L': -1,'R': 1}
    for i in range(0, len(commands)):
        assert(commands[i] in ['G', 'L', 'R'])
        if commands[i] == 'R' or commands[i] == 'L':
            currDir = getDirection(currDir, commands[i], direction)
        elif commands[i] == 'G':
            if currDir == 0:
                y += 1
            elif currDir == 1:
                x += 1
            elif currDir == 2:
                y -= 1
            elif currDir == 3:
                x -= 1
    return x, y, currDir

def getDirection(currentDirection, newDirectionTag, direction):
    assert (currentDirection in [0,1,2,3])
    return (currentDirection + direction[newDirectionTag]) % 4


print doesCircleExist('GRGRGR')
print doesCircleExist('GRGLLG')
print doesCircleExist('GRG')
print doesCircleExist('G')
print doesCircleExist('R')
print doesCircleExist('GGRRGGRRGGLLGGLL')
print doesCircleExist('RGRGRGRGL')
print doesCircleExist('RRRRRL')
