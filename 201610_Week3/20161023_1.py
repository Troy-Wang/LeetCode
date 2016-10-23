"""
Remove Duplicates from Sorted Array
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentNum = None
        currentIndex = 0
        for eachNum in nums:
            if eachNum != currentNum:
                nums[currentIndex] = eachNum
                currentIndex += 1
                currentNum = eachNum
        return currentIndex


solution = Solution()
print(solution.removeDuplicates([]))
