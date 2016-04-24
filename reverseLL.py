# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        prev = None
        ptr = head
        while ptr.next != None:
            fwd = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = fwd
        ptr.next = prev
        head = ptr
        return head
