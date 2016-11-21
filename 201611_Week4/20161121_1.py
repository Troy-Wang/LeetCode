"""
89. Gray Code
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in range(0, 1 << n):
            ret.append(i ^ (i >> 1))
        return ret


solution = Solution()
print(solution.grayCode(0))
