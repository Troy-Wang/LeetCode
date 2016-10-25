"""
Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        flag = 0
        for eachAlph in s:
            if eachAlph == ' ':
                flag = 1
            elif flag == 1:
                count = 1
                flag = 0
            else:
                count += 1
        return count


solution = Solution()
print(solution.lengthOfLastWord(''))
