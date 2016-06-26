class TemperatureTracker(object):
    def __init__(self):
        self._tempList = []
        self._length = 0
        self._sum = 0
        self._mean = 0
        self._tempHash = {}

    def insert(self, tempVal):
        if tempVal < 0 or tempVal > 110:
            raise AttributeError('temp should be within 0 and 110')
        i = 0
        while i < len(self._tempList):
            if tempVal == self._tempList[i][0]:
                self._tempList[i] = (tempVal, self._tempList[i][1] + 1)
            i += 1
        if i == len(self._tempList):
            self._tempList.append((tempVal, 1))
        self._tempList = sorted(self._tempList, key = lambda x: x[0])
        self._length = len(self._tempList)
        self._sum = self._sum + tempVal
        self._mean = 1.0 * self._sum / self._length

    def getMin(self):
        if self._length > 0:
            return self._tempList[0][0]
        return None

    def getMax(self):
        if self._length > 0:
            return self._tempList[self._length - 1][0]
        return None

    def getMean(self):
        if self._length > 0:
            return self._mean
        return None

    def getMode(self):
        modeCount = 0
        mode = 0
        for tempVal, count in self._tempList:
            if count > modeCount:
                modeCount = count
                mode = tempVal
        if self._length > 0:
            return mode
        return None

temp = TemperatureTracker()
temp.insert(2)
temp.insert(3)
temp.insert(5)
temp.insert(2)
temp.insert(6)
temp.insert(0)
print temp.getMax()
print temp.getMin()
print temp.getMean()
print temp.getMode()
