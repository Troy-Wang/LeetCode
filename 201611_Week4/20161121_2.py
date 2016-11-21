"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

    def searchInsert2(self, nums, target):
        if not nums:
            return 0
        return self.searchInsertBinary(nums, 0, len(nums) - 1, target)

    def searchInsertBinary(self, nums, begin, end, target):
        mid = (begin + end) // 2
        if nums[mid] == target:
            return mid
        elif begin >= end and nums[mid] > target:
            return mid
        elif begin >= end and nums[mid] < target:
            return mid + 1
        elif nums[mid] > target:
            return self.searchInsertBinary(nums, begin, mid, target)
        else:
            return self.searchInsertBinary(nums, mid + 1, end, target)


solution = Solution()
print(solution.searchInsert2([1, 3, 5], 4))
