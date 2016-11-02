"""
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):

        buff = {}
        for i in range(len(nums)):
            if nums[i] not in buff.keys():
                buff[target - nums[i]] = i
            else:
                return [buff[nums[i]], i]


solution = Solution()
print(solution.twoSum([], 22))
