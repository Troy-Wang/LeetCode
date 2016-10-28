"""
Third Maximum Number
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        container = []
        for eachNum in nums:
            if len(container) < 3:
                if eachNum not in container:
                    container.append(eachNum)
            elif eachNum > min(container) and eachNum not in container:
                container.remove(min(container))
                container.append(eachNum)

        if len(container) < 3:
            return max(container)
        else:
            return min(container)


solution = Solution()
print(solution.thirdMax([1, -2147483648, 2]))
