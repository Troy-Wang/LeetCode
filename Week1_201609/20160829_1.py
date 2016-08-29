"""Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1."""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        tempSet = []
        for eachLetter in s:
            if eachLetter not in s[count + 1:] and eachLetter not in tempSet:
                return count
            count += 1
            tempSet.append(eachLetter)
        return -1


solution = Solution()
print solution.firstUniqChar('cc')
