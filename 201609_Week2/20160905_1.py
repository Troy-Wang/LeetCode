"""
Given two arrays, write a function to compute their intersection.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numDict = {}
        for eachNum in nums1:
            numDict[eachNum] = 1

        retDict = {}
        for eachNum in nums2:
            if eachNum in numDict.keys() and eachNum not in retDict.keys():
                retDict[eachNum] = 1

        return retDict.keys()


solution = Solution()
nums1 = []
nums2 = []
print(solution.intersection(nums1, nums2))
