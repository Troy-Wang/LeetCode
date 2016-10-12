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

    def productExceptSelf2(self, nums):
        totalProduct = 1
        ret = []
        for eachNum in nums:
            totalProduct *= eachNum
        for i in range(len(nums)):
            ret.append(self.divide(totalProduct, nums[i]))
        return ret

    def divide(self, a, b):
        count = 0
        while a >= b:
            a = a - b
            count += 1
        return count


solution = Solution()
print(solution.productExceptSelf([5, 2, 3, 4, 1, 7]))
print(solution.productExceptSelf2([5, 2, 3, 4, 1, 7]))
