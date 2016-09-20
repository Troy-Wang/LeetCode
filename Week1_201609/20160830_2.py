"""Given an array of integers, every element appears twice except for one.
Find that single one.Given an array of integers, every element appears twice except for one.
 Find that single one."""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for eachNum in nums:
            result ^= eachNum
        return result


solution = Solution()
print(solution.singleNumber([2]))
