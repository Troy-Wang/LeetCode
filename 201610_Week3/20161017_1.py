"""
Swap Nodes in Pairs
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
        p = head
        if not p:
            return None
        q = p.next
        if not q:
            return p
        p.next = self.swapPairs(q.next)
        q.next = p
        return q


solution = Solution()
head = ListNode(3)
print(solution.swapPairs(head))
