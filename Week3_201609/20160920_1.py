"""
Given a non negative integer number num. For every numbers i in the range 0 <=i <= num
calculate the number of 1s in their binary representation and return them as an array.
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = []
        current = 0
        while current <= num:
            count = 0
            temp = current
            while temp:
                temp &= temp - 1
                count += 1
            ret.append(count)
            current += 1
        return ret

    def countBits2(self, num):
        ret = [0]
        current = 1
        while current <= num:
            ret.append(ret[current / 2] + current % 2)
            current += 1
        return ret


solution = Solution()
print solution.countBits2(0)
