"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.indexPlusOne(digits, len(digits) - 1)
        return digits

    def indexPlusOne(self, digits, index):
        if index < 0:
            digits.insert(0, 1)
            return
        digits[index] = (digits[index] + 1) % 10
        if digits[index] == 0:
            self.indexPlusOne(digits, index - 1)


solution = Solution()
print solution.plusOne([9, 9, 9])
