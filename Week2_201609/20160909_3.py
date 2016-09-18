"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has
(also known as the Hamming weight).
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


solution = Solution()
print solution.hammingWeight(11)