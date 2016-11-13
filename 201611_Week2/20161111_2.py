"""
413. Arithmetic Slices
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        step = []
        count = 0
        previous = None
        for i in range(len(A) - 1):
            current = A[i + 1] - A[i]
            if current == previous:
                count += 1
            elif count >= 1:
                step.append(count)
                count = 0
            else:
                count = 0
            previous = current
        if count >= 1:
            step.append(count)

        ret = 0
        for eachNum in step:
            ret += eachNum * (eachNum + 1) // 2
        return ret


solution = Solution()
print(solution.numberOfArithmeticSlices([1, 2, 4, 6, 8, 12, 16, 20, 24]))
