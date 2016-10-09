"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.
"""
import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(row[0], row, 1) for row in matrix]
        heapq.heapify(heap)

        for _ in range(k - 1):
            rowHead, r, index = heap[0]
            if index < len(r):
                heapq.heapreplace(heap, (r[index], r, index + 1))
            else:
                heapq.heappop(heap)

        return heap[0][0]

    def kthSmallest2(self, matrix, k):
        return list(heapq.merge(*matrix))[k-1]


solution = Solution()
print(solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(solution.kthSmallest2([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
