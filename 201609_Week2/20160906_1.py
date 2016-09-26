import string


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphDict = {}
        count = 1
        for eachAlph in string.uppercase:
            alphDict[eachAlph] = count
            count += 1

        ret = 0
        for i, j in enumerate(reversed(list(s))):
            ret += (26 ** i) * alphDict[j]
        return ret


solution = Solution()
print(solution.titleToNumber('Z'))
