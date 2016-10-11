"""
Product of Array Except Self
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is
equal to the product of all the elements of nums except nums[i].
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current = 1
        ret = []
        for i in range(len(nums)):
            ret.append(current)
            current *= nums[i]
        current = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= current
            current *= nums[i]
        return ret


solution = Solution()
print(solution.productExceptSelf([5, 2, 3, 4, 1, 7]))
