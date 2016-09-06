"""
Given two strings s and t, write a function to determine if t is an anagram of s.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        sLen = 0
        for eachLetter in s:
            sLen += 1
            if eachLetter not in sDict.keys():
                sDict[eachLetter] = 1
            else:
                sDict[eachLetter] += 1

        tLen = 0
        for eachLetter in t:
            tLen += 1
            if eachLetter not in sDict.keys() or sDict[eachLetter] == 0:
                return False
            else:
                sDict[eachLetter] -= 1

        if tLen != sLen:
            return False
        return True


solution = Solution()
print solution.isAnagram('a', 'a')
