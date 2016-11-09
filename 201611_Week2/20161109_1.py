"""
Two Sum II - Input array is sorted
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        l = 0
        h = length - 1
        while l < h:
            if numbers[l] + numbers[h] < target:
                l += 1
            elif numbers[l] + numbers[h] > target:
                h -= 1
            else:
                return l + 1, h + 1


solution = Solution()
print(solution.twoSum([1, 3, 6, 8, 9], 9))
