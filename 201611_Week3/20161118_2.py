class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        digit = ''
        for eachDigit in s:
            if eachDigit != ']':
                if '0' <= eachDigit <= '9':
                    digit += eachDigit
                else:
                    stack.append(digit)
                    stack.append(eachDigit)
                    digit = ''
            else:
                current = stack.pop()
                string = ''
                while current != '[':
                    string = current + string
                    current = stack.pop()
                stack.extend(list(int(stack.pop()) * string))
        return ''.join(stack)


solution = Solution()
print(solution.decodeString('10[a2[c]]'))
