"""
Lowest Common Ancestor of a Binary Search Tree
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not p:
            return q
        if not q:
            return p

        if (p.val - root.val) * (q.val - root.val) < 0:
            return root
        elif (p.val - root.val) * (q.val - root.val) == 0:
            return root
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
h = TreeNode(3)
i = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i
solution = Solution()
print(solution.lowestCommonAncestor(a, c, g).val)
