# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

        if not root:
            return

        stack = []
        ret = []
        stack.append(root)

        while stack:
            current = stack.pop()
            if not current.left and not current.right:
                print(stack)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


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
print(solution.binaryTreePaths(a))
