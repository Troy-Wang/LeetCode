"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonPrefix = '' if not strs else strs[0]
        for eachStr in strs:
            count = 0
            while count < len(commonPrefix) and count < len(eachStr):
                if commonPrefix[count] == eachStr[count]:
                    count += 1
                else:
                    break
            commonPrefix = commonPrefix[:count]
        return commonPrefix


solution = Solution()
print(solution.longestCommonPrefix(['12345', '123', '1', '12456']))
