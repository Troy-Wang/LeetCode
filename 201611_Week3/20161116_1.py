"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.addParenthese(ret, '', n, 0)
        return ret

    def addParenthese(self, ret, parenthese, leftCount, rightCount):
        if not leftCount and not rightCount:
            ret.append(parenthese)
            return

        if leftCount > 0:
            self.addParenthese(ret, parenthese + '(', leftCount - 1, rightCount + 1)
        if rightCount > 0:
            self.addParenthese(ret, parenthese + ')', leftCount, rightCount - 1)


solution = Solution()
print(solution.generateParenthesis(3))
