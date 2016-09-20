"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for eachNum in nums:
            if eachNum != val:
                nums[i] = eachNum
                i += 1
        return nums[:i]


solution = Solution()
print(solution.removeElement([3, 2, 2, 3, 1, 2], 3))
