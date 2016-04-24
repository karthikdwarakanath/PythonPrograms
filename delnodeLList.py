#Given a linked list, remove the nth node from the end of list and return its head.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        ptr1 = head
        ptr2 = head
        if n == 1:
            ptr1 = ptr1.next
            while ptr1.next != None:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            ptr2.next = None
            return head
        while n > 1:
            ptr1 = ptr1.next
            n = n-1
        while ptr1.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr2 == head:
            return head.next
        else:
            ptr2.val = ptr2.next.val
            ptr2.next = ptr2.next.next
            return head
