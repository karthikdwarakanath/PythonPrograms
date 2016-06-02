# implement a stack, with push, pop and findminimum function
class Stack(object):
    def __init__(self):
        self.arr = []
        self.tmpArr = []

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False

    def push(self, value):
        self.arr.append(value)
        if len(self.tmpArr) == 0:
            self.tmpArr.append(value)
        elif value < self.findMinimum():
            self.tmpArr.append(value)

    def pop(self):
        if not self.isEmpty():
            itemPopped = self.arr.pop()
            if itemPopped == self.findMinimum():
                self.tmpArr.pop()
            return itemPopped
        else:
            return None

    def findMinimum(self):
        if len(self.tmpArr) > 0:
            return self.tmpArr[len(self.tmpArr) - 1]
        else:
            return None

    def display(self):
        return self.arr, self.tmpArr

new = Stack()
new.push(2)
new.push(3)
new.push(1)
new.push(5)
new.push(4)
print new.display()
print 'min'
print new.findMinimum()
print new.pop()
print 'min'
print new.findMinimum()
print new.pop()
print 'min'
print new.findMinimum()
print new.pop()
print 'min'
print new.findMinimum()
print new.pop()
print 'min'
print new.findMinimum()
print new.pop()
print 'min'
print new.findMinimum()
print new.pop()
