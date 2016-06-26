#Given a root node, check if the tree is a BST or not
#Just the relatioship between immediate parent sibling is not enough
#Need to check for the max and min value possible for the child node

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


NEGINF=float("infinity")
INF = float("-infinity")

def isBST(root):
    return isBSTHelper(root, NEGINF, INF)

def isBSTHelper(root, minVal, maxVal):
    if not root:
        return True
    if not (minVal <= root.value <= maxVal):
        return False
    return isBSTHelper(root.left, minVal, root.value) and isBSTHelper(root.right, root.value, maxVal)
