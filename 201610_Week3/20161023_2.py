"""
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        preHead = ListNode(-1)
        preHead.next = head
        index = preHead
        count = 0
        current = None
        while index.next:
            index = index.next
            count += 1
            if count == n:
                current = preHead
            elif count > n:
                current = current.next
        if current:
            current.next = current.next.next
        return preHead.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
solution = Solution()
solution.removeNthFromEnd(a, 9)
current = a
while current:
    print(current.val)
    current = current.next
