"""
Valid Parentheses
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        pre = list('{[(')
        stack = []
        for each_bit in l:
            if each_bit in pre:
                stack.append(each_bit)
            elif not len(stack) or not self.isPair(each_bit, stack.pop()):
                return False
        if stack:
            return False
        return True

    def isPair(self, input1, input2):
        dict = {'{': '1', '}': '1', '[': '2', ']': '2', '(': '3', ')': '3'}
        if dict.get(input1) == dict.get(input2):
            return True


solution = Solution()
print(solution.isValid('['))
