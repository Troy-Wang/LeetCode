"""
384. Shuffle an Array
"""
import copy
import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.original = nums
        self.shuffled = copy.deepcopy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.shuffled) - 1, 0, -1):
            ran = random.randint(0, i)
            self.shuffled[i], self.shuffled[ran] = self.shuffled[ran], self.shuffled[i]
        return self.shuffled


obj = Solution([1, 2, 3, 4, 5, 6, 7, 8, 9])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1)
print(param_2)
