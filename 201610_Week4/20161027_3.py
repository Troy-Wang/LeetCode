import gc


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        currentA = headA
        currentB = headB
        while currentA:
            currentA = currentA.next
            lenA += 1
        while currentB:
            currentB = currentB.next
            lenB += 1

        count = 0
        currentA = headA
        currentB = headB
        if lenA > lenB:
            while count < lenA - lenB:
                currentA = currentA.next
                count += 1
        else:
            while count < lenB - lenA:
                currentB = currentB.next
                count += 1

        while currentA != currentB:
            currentA = currentA.next
            currentB = currentB.next

        gc.collect()
        return currentA

    def getIntersectionNode2(self, headA, headB):

        currentA = headA
        currentB = headB
        while currentA != currentB:
            currentA = headB if not currentA else currentA.next
            currentB = headA if not currentB else currentB.next
        gc.collect()
        return currentA


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)
b1 = ListNode(7)
b2 = ListNode(8)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
b1.next = b2
b2.next = a4

solution = Solution()
print(solution.getIntersectionNode2(a1, b1))
