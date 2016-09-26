"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        for eachNum in nums:
            if numDict.has_key(eachNum):
                return True
            else:
                numDict[eachNum] = 1

        return False

solution = Solution()
print(solution.containsDuplicate([6, 5]))
