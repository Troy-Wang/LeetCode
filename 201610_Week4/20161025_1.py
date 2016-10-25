"""
Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        preHead = ListNode(-1)
        preHead.next = head
        current = preHead
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return preHead.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(5)
f = ListNode(6)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
solution = Solution()
current = solution.removeElements(a, 1)
while current:
    print(current.val)
    current = current.next
