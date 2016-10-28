"""
Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n > 0:
            ret += n // 5
            n //= 5
        return ret


solution = Solution()
print(solution.trailingZeroes(77))
