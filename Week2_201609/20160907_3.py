"""
Given two arrays, write a function to compute their intersection.
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        aDict = {}
        for eachNum in nums1:
            if aDict.has_key(eachNum):
                aDict[eachNum] += 1
            else:
                aDict[eachNum] = 1

        ret = []
        for eachNum in nums2:
            if aDict.has_key(eachNum) and aDict[eachNum] > 0:
                ret.append(eachNum)
                aDict[eachNum] -= 1

        return ret


solution = Solution()
print(solution.intersect([1, 2], [1]))
