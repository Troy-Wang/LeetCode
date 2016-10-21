"""
Count and Say
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current_say = ['1']
        for i in range(2, n + 1):
            count = 0
            current_digit = current_say[0]
            next_say = []
            for each_digit in current_say:
                if each_digit == current_digit:
                    count += 1
                else:
                    next_say.append(str(count))
                    next_say.append(str(current_digit))
                    current_digit = each_digit
                    count = 1
            next_say.append(str(count))
            next_say.append(str(current_digit))
            current_say = next_say
        return ''.join(current_say)


solution = Solution()
print(solution.countAndSay(7))
