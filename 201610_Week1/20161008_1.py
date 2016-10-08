"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        hasZero = False
        currentSum = 0
        for eachNum in nums:
            currentSum += eachNum
            if eachNum > max:
                max = eachNum
            if eachNum == 0:
                hasZero = True

        ret = int(max * (max + 1) / 2 - currentSum)
        if hasZero and ret == 0:
            return max + 1
        else:
            return ret


solution = Solution()
print(solution.missingNumber([0, 1]))
