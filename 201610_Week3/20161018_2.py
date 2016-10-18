"""
Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(1, n + 1):
            if self.multify3(i) and self.multify5(i):
                ret.append('FizzBuzz')
            elif self.multify3(i):
                ret.append('Fizz')
            elif self.multify5(i):
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret

    def multify5(self, num):
        if not num % 5:
            return True

    def multify3(self, num):
        if not num % 3:
            return True


solution = Solution()
print(solution.fizzBuzz(1))
