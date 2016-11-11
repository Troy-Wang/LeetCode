# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        current = root
        while current:
            stack.append((current, False))
            current = current.left

        while stack:
            current, visited = stack.pop()
            if not current.right or visited:
                ret.append(current.val)
            else:
                stack.append((current, True))
                current = current.right
                while current:
                    stack.append((current, 0))
                    current = current.left
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
print(solution.postorderTraversal(a))
