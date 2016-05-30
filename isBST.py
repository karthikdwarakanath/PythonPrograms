#Given a root node, check if the tree is a BST or not
#Just the relatioship between immediate parent sibling is not enough
#Need to check for the max and min value possible for the child node

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isBST(root):
    return isBSTHelper(root, min, max)

def isBSTHelper(curr, min, max):
    if curr.left:
        if curr.left.value < min or not isBSTHelper(curr.left, min, curr.value):
            return False
    if curr.right:
        if curr.right.value > max or not isBSTHelper(curr.right, curr.value, max):
            return False
    return True
