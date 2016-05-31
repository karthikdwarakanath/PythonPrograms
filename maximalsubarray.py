class MaximalSubArray(object):
    def __init__(self, arr):
        self.arr = arr

    def findMaxSub(self):
        x, y, z = 0, 0, 0
        maxy, loc = 0, 0
        for i in range(0, len(self.arr)):
            x = x + self.arr[i]
            y = min(y, x)
            z = x - y
            thisfunc = lambda: (z, i) if (z > maxy) else (maxy, loc)
            maxy, loc = thisfunc()
        finalArr = []
        c = loc
        while maxy != 0:
            maxy = maxy - self.arr[c]
            c = c - 1
        return self.arr[c+1:loc+1]

sd = MaximalSubArray([1,-3,5,-2,9,-8, -6,4])
print sd.findMaxSub()
