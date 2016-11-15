"""
318. Maximum Product of Word Lengths
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxMulti = 0
        for i in range(0, len(words) - 1):
            length1 = len(words[i])
            minLength2 = 0
            for j in range(i + 1, len(words)):
                if len(words[j]) > minLength2 and not (set(words[i]) & set(words[j])):
                    maxMulti = max(maxMulti, length1 * len(words[j]))
        return maxMulti

    def maxProduct2(self, words):
        maskDict = {}
        for eachWord in words:
            mask = 0
            for eachByte in eachWord:
                mask |= 1 << (ord(eachByte) - 97)
            maskDict[mask] = max(maskDict.get(mask, 0), len(eachWord))
        return max([maskDict[i] * maskDict[j] for i in maskDict for j in maskDict if not i & j] or [0])


solution = Solution()
print(solution.maxProduct2(["a", "aa", "aaaa", "a", "a", "a"]))
