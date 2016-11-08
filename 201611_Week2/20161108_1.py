"""
Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.
"""

import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for eachNum in nums:
            dic.setdefault(eachNum, 0)
            dic[eachNum] += 1

        return heapq.nlargest(k, dic, lambda key: dic[key])

    def topKFrequent2(self, nums, k):
        return [item[0] for item in collections.Counter(nums).most_common(k)]


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 4, 1, 2, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6], 3))
