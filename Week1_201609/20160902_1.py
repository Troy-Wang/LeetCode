"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i, j in enumerate(nums):
            if j != 0:
                nums[i] = 0
                nums[count] = j
                count += 1


solution = Solution()
nums = [0, 1, 2, 0, 3, 0, 4, 5, 6, 0, 0, 0]
solution.moveZeroes(nums)
print(nums)
