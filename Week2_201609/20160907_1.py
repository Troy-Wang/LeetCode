"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) / 2]


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for eachNum in nums[1:]:
            if count == 0:
                major = eachNum
                count += 1
            elif eachNum == major:
                count += 1
            else:
                count -= 1

        return major


solution = Solution1()
print solution.majorityElement([1, 2, 3, 3, 3])

solution = Solution2()
print solution.majorityElement([6, 5, 5])
