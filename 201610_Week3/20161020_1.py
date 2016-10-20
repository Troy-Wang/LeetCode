"""
Nth Digit
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        count = 0
        while num > 0:
            num -= 9 * (10 ** count) * (count + 1)
            count += 1

        bits = count - 1
        bitsSumBefore = 0
        for i in range(1, bits + 1):
            bitsSumBefore += 10 ** (i - 1) * 9 * i

        (ret1, ret2) = divmod(n - bitsSumBefore, bits + 1)

        return int(str(10 ** bits + ret1 - 1)[bits]) if ret2 == 0 else int(str(10 ** bits + ret1)[ret2 - 1])

    def findNthDigit2(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        count = 0
        while num > 0:
            num -= 9 * (10 ** count) * (count + 1)
            count += 1

        bits = count - 1

        (ret1, ret2) = divmod(num + 9 * (10 ** bits) * count, bits + 1)

        return int(str(10 ** bits + ret1 - 1)[bits]) if ret2 == 0 else int(str(10 ** bits + ret1)[ret2 - 1])


solution = Solution()
print(solution.findNthDigit(12313212313))
print(solution.findNthDigit2(12313212313))
