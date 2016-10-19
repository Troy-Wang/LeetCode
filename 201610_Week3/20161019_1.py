"""
Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.areSymmetric(root.left, root.right)

    def areSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and self.areSymmetric(left.left, right.right) \
               and self.areSymmetric(left.right, right.left)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
solution = Solution()
print(solution.isSymmetric(a))
