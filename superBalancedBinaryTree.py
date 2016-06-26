class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

bt = BinaryTreeNode(4)
bt1 = bt.insert_left(3)
bt2 = bt.insert_right(5)
bt3 = bt1.insert_left(7)
bt4 = bt1.insert_right(8)
bt5 = bt2.insert_left(11)
bt6 = bt2.insert_right(12)

print bt.value, bt1.value, bt2.value, bt3.value, bt4.value, bt5.value, bt6.value

def minLevel(BT):
    if not BT:
        return 0
    return min(minLevel(BT.left), minLevel(BT.right)) + 1

def maxLevel(BT):
    if not BT:
        return 0
    return max(maxLevel(BT.left), maxLevel(BT.right)) + 1

def isBalanced(maxlevel, minlevel):
    if maxlevel - minlevel <= 1:
        return True
    return False
