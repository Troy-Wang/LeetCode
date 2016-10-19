"""
Pascal's Triangle
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascalTri = []
        for i in range(1, numRows + 1):
            singleRow = [1]
            s = 1
            for j in range(2, i):
                s = (i - j + 1) * s // (j - 1)
                singleRow.append(s)
            if i != 1:
                singleRow.append(1)
            pascalTri.append(singleRow)
        return pascalTri


solution = Solution()
print(solution.generate(5))
