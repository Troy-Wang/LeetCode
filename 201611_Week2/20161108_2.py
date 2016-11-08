"""
Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n > 10:
            n = 10
        count = 0
        current = 1
        for i in range(n - 1):
            current *= 9 - i
            count += current
        return count * 9 + 10
