"""
Given a linked list, swap every two adjacent nodes and return its head.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        head = p.next
        while p:
            q = p.next
            p.next = q.next
            q.next = p
            p = p.next
        return head
