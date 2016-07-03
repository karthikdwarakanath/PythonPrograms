from collections import deque

def dfs(root, val):
   qu = deque()
   if root.val == val:
      return True
   if root:
      qu.append(root)
   while not qu.empty():
      node = qu.dequeue
      if node:
         visit(node)
         if node.val == value:
            return True
         qu.append(node.left)
         qu.append(node.right)
    return False
