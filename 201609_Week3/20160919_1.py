"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
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
            levelNode = []
            while current < last:
                levelNode.append(queue[current].val)
                if queue[current].left:
                    queue.append(queue[current].left)
                if queue[current].right:
                    queue.append(queue[current].right)
                current += 1
            ret.append(levelNode)
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
print(solution.levelOrder(a))
