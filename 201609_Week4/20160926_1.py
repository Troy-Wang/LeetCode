"""
Given two binary strings, return their sum (also a binary string).
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        addOn = 0
        aList = list(a)
        bList = list(b)
        ret = ""
        while aList or bList:
            if not len(aList):
                aBit = 0
            else:
                aBit = aList.pop()
            if not len(bList):
                bBit = 0
            else:
                bBit = bList.pop()
            bitRet = int(aBit) + int(bBit) + addOn
            (addOn, bit) = divmod(bitRet, 2)
            ret = str(bit) + ret
        if addOn:
            ret = '1' + ret
        return ret


solution = Solution()
print(solution.addBinary("110", '11'))
