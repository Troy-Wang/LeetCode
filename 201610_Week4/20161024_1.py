"""
Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        currentIndex = m + n - 1
        index1 = m - 1
        index2 = n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[currentIndex] = nums1[index1]
                index1 -= 1
                currentIndex -= 1
            else:
                nums1[currentIndex] = nums2[index2]
                index2 -= 1
                currentIndex -= 1
        while index2 >= 0:
            nums1[currentIndex] = nums2[index2]
            index2 -= 1
            currentIndex -= 1
        return nums1


solution = Solution()
print(solution.merge([1, 2, 3, 4, 9, 0, 0, 0, 0, 0], 0, [5, 6, 7, 8, 10], 5))
