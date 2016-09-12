"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        sList = list(s)
        stack = []
        for eachLetter in s:
            if eachLetter in vowels:
                stack.append(eachLetter)

        for index, letter in enumerate(s):
            if letter in vowels:
                sList[index] = stack.pop()

        return ''.join(sList)

    def reverseVowels2(self, s):
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        sList = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if sList[i] not in vowels:
                i += 1
            elif sList[j] not in vowels:
                j -= 1
            else:
                tmp = sList[i]
                sList[i] = sList[j]
                sList[j] = tmp
                i += 1
                j -= 1
        return ''.join(sList)


solution = Solution()
print solution.reverseVowels2('')
