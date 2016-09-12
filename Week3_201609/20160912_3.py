"""
Given a linked list, determine if it has a cycle in it.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        p = head
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = b
# d.next = e
# e.next = b
solution = Solution()
print solution.hasCycle(a)
