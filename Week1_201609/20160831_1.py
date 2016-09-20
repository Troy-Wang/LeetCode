"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    myNum = 6

    def guess(self, yourNum):
        if yourNum < self.myNum:
            return 1
        elif yourNum > self.myNum:
            return -1
        else:
            return 0

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n + 1
        while s < e:
            mid = (s + e) / 2
            if self.guess(mid) == 0:
                return mid
            elif self.guess(mid) == -1:
                e = mid
            else:
                s = mid


solution = Solution()
solution.myNum = 12
print(solution.guessNumber(14))
