"""
421. Maximum XOR of Two Numbers in an Array
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(32, -1, -1):
            ret <<= 1
            prefix = {num >> i for num in nums}
            ret += any(ret ^ 1 ^ p in prefix for p in prefix)
        return ret


solution = Solution()
print(solution.findMaximumXOR([3, 10, 5, 25, 2, 8]))
