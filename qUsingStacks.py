#implement queue using stacks

class Stack(object):
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        return self.arr.pop()

ins = Stack([])
out = Stack([])

def enqu(value):
    while not out.isEmpty():
        ins.push(out.pop())
    ins.push(value)

def dequ():
    while not ins.isEmpty():
        out.push(ins.pop())
    return out.pop()
