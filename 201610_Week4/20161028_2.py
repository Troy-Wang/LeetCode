"""
Rotate Function
"""


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sumA = sum(A)
        lenA = len(A)
        count = 0
        ret = 0
        for eachNum in A:
            ret += count * eachNum
            count += 1

        current = ret
        for i in range(1, lenA):
            current = current + sumA - lenA * A[lenA - i]
            ret = max(ret, current)

        return ret


solution = Solution()
print(solution.maxRotateFunction([4, 3, 2, 6]))
