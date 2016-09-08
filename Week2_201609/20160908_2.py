"""
Given an integer, write a function to determine if it is a power of three.
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** 19 % n == 0


solution = Solution()
print solution.isPowerOfThree(243)
