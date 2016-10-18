"""
Ugly Number
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Note that 1 is typically treated as an ugly number.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 5 == 0:
            return self.isUgly(num / 5)
        if num % 3 == 0:
            return self.isUgly(num / 3)
        if num % 2 == 0:
            return self.isUgly(num / 2)
        return False


solution = Solution()
print(solution.isUgly(44))
