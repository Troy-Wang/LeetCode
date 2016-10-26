"""

"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        current = n
        ret = 0
        for i in range(0, 32):
            ret += 2 ** (31 - i) * (current % 2)
            current >>= 1
        return ret

    def reverseBits2(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


solution = Solution()
print(solution.reverseBits2(43261596))
