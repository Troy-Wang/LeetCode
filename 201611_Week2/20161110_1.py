# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            if stack:
                current = stack.pop()
                ret.append(current.val)
                current = current.right

        return ret


a = TreeNode(1)
b = TreeNode(4)
c = TreeNode(11)
d = TreeNode(6)
e = TreeNode(7)
f = TreeNode(2)
g = TreeNode(3)
a.left = b
b.left = c
b.right = d
c.left = e
c.right = f
d.left = g
solution = Solution()
print(solution.inorderTraversal(a))
