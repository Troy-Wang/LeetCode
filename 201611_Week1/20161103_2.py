class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numLen = len(nums)
        for i in range(k % numLen):
            nums.insert(0, nums.pop())

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[0:k].reverse()
        nums[k:len(nums)].reverse()


solution = Solution()
print(solution.rotate2([1, 2, 3, 4, 5], 7))
