"""
153. Find Minimum in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]

    def findMin2(self, nums):
        if not nums:
            return None
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[start] < nums[end]:
                return nums[start]
            if nums[start] <= nums[mid]:
                start = mid + 1
            elif nums[start] > nums[mid]:
                end = mid
        return nums[start]


solution = Solution()
print(solution.findMin2([2, 1]))
