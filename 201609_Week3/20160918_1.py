"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        queue = [root]
        current = 0
        last = 1
        while current < len(queue):
            last = len(queue)
            levelList = []
            while current < last:
                levelList.append(queue[current].val)
                if queue[current].left:
                    queue.append(queue[current].left)
                if queue[current].right:
                    queue.append(queue[current].right)
                current += 1
            ret.insert(0, levelList)
        return ret


solution = Solution()
a = TreeNode(3)
# b = TreeNode(9)
# c = TreeNode(20)
# d = TreeNode(15)
# e = TreeNode(7)
# a.left = b
# a.right = c
# c.left = d
# c.right = e
print(solution.levelOrderBottom(a))
