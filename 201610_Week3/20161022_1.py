"""
Word Pattern
Given a pattern and a string str, find if str follows the same pattern.
pattern = "abba", str = "dog cat cat dog" should return true.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.isSameSet(self.analysisPattern(pattern), self.analysisPattern(str.split()))

    def wordPattern2(self, pattern, str):
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))

    def analysisPattern(self, pattern):
        dict = {}
        count = 0
        for eachDigit in pattern:
            if eachDigit not in dict.keys():
                dict[eachDigit] = [count]
            else:
                dict[eachDigit].append(count)
            count += 1
        return dict.values()

    def isSameSet(self, set1, set2):
        if len(set1) != len(set2):
            return False
        for i in set1:
            if i not in set2:
                return False
        return True


solution = Solution()
print(solution.wordPattern2('abbc', 'cat dog dog ee'))
