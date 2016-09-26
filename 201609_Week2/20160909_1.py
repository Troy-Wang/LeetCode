"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sqDict = {}
        sqSum = n
        while sqSum != 1:
            sqSum = self.calcDigitSum(sqSum)
            print(sqSum)
            if sqDict.has_key(sqSum):
                return False
            else:
                sqDict[sqSum] = 1
        return True

    def calcDigitSum(self, n):
        sqSum = 0
        while n:
            sqSum += (n % 10) ** 2
            n /= 10
        return sqSum


solution = Solution()
print(solution.isHappy(111))
