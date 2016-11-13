"""
406. Queue Reconstruction by Height
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        ret = []
        for eachPerson in people:
            inserted = False
            count = 0
            for i in range(len(ret)):
                if ret[i][0] >= eachPerson[0]:
                    count += 1
                if count > eachPerson[1]:
                    ret.insert(i, eachPerson)
                    inserted = True
                    break
                elif count == eachPerson[1]:
                    ret.insert(i + 1, eachPerson)
                    inserted = True
                    break
            if not inserted:
                ret.append(eachPerson)
        return ret


solution = Solution()
print(solution.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# print(solution.reconstructQueue([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]))
