"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        twoNumsXor = self.calcXor(nums)
        ret1 = 0
        ret2 = 0
        count = self.getNotZeroBit(twoNumsXor)
        for eachNum in nums:
            if (eachNum >> count) % 2:
                ret1 ^= eachNum
            else:
                ret2 ^= eachNum

        return [ret1, ret2]

    def calcXor(self, nums):
        ret = 0
        for eachNum in nums:
            ret ^= eachNum
        return ret

    def getNotZeroBit(self, num):
        count = 0
        while not num % 2:
            num >>= 1
            count += 1
        return count


solution = Solution()
print(solution.singleNumber([1, 2, 1, 3, 2, 5]))
