"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 is None or (l1 is not None and l1.val < l2.val):
            head = l1
            p = l1
            q = l2
        else:
            head = l2
            p = l2
            q = l1

        while p and q:
            if p.next is None or p.val <= q.val <= p.next.val:
                tmp = q.next
                q.next = p.next
                p.next = q
                p = q
                q = tmp
            elif q.val > p.next.val:
                p = p.next

        return head


a1 = ListNode(2)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(1)
a5 = ListNode(2)
a6 = ListNode(3)
a1.next = a2
a2.next = a3
a4.next = a5
a5.next = a6

solution = Solution()
head = solution.mergeTwoLists(a1, a4)
while head:
    print head.val
    head = head.next
