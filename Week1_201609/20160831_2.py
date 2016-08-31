class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mLetters = {}
        for eachLetter in magazine:
            if eachLetter not in mLetters.keys():
                mLetters[eachLetter] = 1
            else:
                mLetters[eachLetter] += 1

        for eachLetter in ransomNote:
            if eachLetter not in mLetters.keys():
                return False
            else:
                mLetters[eachLetter] -= 1
                if mLetters[eachLetter] < 0:
                    return False

        return True


solution = Solution()
print solution.canConstruct('abcde', 'ebcda')
