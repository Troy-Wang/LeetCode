"""
Longest Palindrome
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        count = 0
        for i in s:
            if i in dic.keys() and dic[i] == 1:
                count += 1
                dic[i] = 0
            else:
                dic[i] = 1
        print(dic)
        for key in dic.keys():
            if dic[key] == 1:
                return count * 2 + 1
        return count * 2


solution = Solution()
print(solution.longestPalindrome('abccccdd'))
