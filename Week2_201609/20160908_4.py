"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
"""
import math


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and 2 ** 15 % math.sqrt(num) == 0


solution = Solution()
print solution.isPowerOfFour(16)
