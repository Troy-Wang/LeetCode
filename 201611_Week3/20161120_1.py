"""
46. Permutations
"""
import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.permutation(ret, 0, nums)
        return ret

    def permutation(self, ret, pos, nums):
        if pos >= len(nums):
            ret.append(copy.copy(nums))
            return
        for i in range(pos, len(nums)):
            nums[pos], nums[i] = nums[i], nums[pos]
            self.permutation(ret, pos + 1, nums)
            nums[i], nums[pos] = nums[pos], nums[i]


solution = Solution()
print(solution.permute([1, 2, 3]))
