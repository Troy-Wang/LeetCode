"""
Add Strings
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        ret = []
        carry = 0
        while index1 >= 0 or index2 >= 0:
            if index1 < 0:
                carry, remainder = divmod(int(num2[index2]) + carry, 10)
            elif index2 < 0:
                carry, remainder = divmod(int(num1[index1]) + carry, 10)
            else:
                carry, remainder = divmod(int(num1[index1]) + int(num2[index2]) + carry, 10)
            index1 -= 1
            index2 -= 1
            ret.insert(0, str(remainder))
        if carry == 1:
            ret.insert(0, '1')
        return ''.join(ret)


solution = Solution()
print(solution.addStrings('99', '2'))
