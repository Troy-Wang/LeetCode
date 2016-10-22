"""
Isomorphic Strings
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.find, s)) == list(map(t.index, t))


solution = Solution()
print(solution.isIsomorphic('add', 'egg'))
