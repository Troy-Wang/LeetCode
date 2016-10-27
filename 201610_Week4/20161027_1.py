"""
Reverse Integer
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1
            x = -x

        ret = 0
        while x != 0:
            ret = ret * 10 + x % 10
            x //= 10

        ret = -ret if flag else ret
        return 0 if abs(ret) > 0x7FFFFFFF else ret


solution = Solution()
print(solution.reverse(-321))
