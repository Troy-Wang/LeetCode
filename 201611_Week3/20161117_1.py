"""
328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        evenHead = ListNode(-1)
        current = head
        currentEven = evenHead
        while current:
            currentEven.next = current.next
            currentEven = currentEven.next
            if currentEven and currentEven.next:
                current.next = currentEven.next
                current = current.next
            else:
                break
        if evenHead.next:
            current.next = evenHead.next
        return head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
seven = ListNode(7)
eight = ListNode(8)
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
solution = Solution()
solution.oddEvenList(one)
current = one
while current:
    print(current.val)
    current = current.next
