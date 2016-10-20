"""
Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        if not rowIndex:
            return ret
        s = 1
        for i in range(1, rowIndex + 1):
            s = (rowIndex - i + 1) * s // i
            ret.append(s)
        return ret


solution = Solution()
print(solution.getRow(0))
