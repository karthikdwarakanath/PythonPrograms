# Implement a moving window avg on a data stream

from collections import deque

class MovingAverage(object):
    def __init__(self, size):
        self.__size = size
        self.__sum = 0
        self.__qu = deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__qu) == self.__size:
            self.__qu.popleft()
        self.__qu.append(val)
        self.__sum = self.__sum + val
        return 1.0 * self.__sum/len(__qu)
