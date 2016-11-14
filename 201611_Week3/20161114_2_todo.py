"""
436. Find Right Interval
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        ret = []
        for i in range(0, len(intervals)):
            index = -1
            currentMin = None
            for j in range(0, len(intervals)):
                if intervals[i].end <= intervals[j].start and (currentMin is None or intervals[j].start < currentMin):
                    index = j
                    currentMin = intervals[j].start
            ret.append(index)
        return ret


solution = Solution()
a = Interval(-2, 0)
b = Interval(-1, 1)
c = Interval(0, 2)
d = Interval(1, 3)
e = Interval(2, 4)
print(solution.findRightInterval([a, b, c, d, e]))
