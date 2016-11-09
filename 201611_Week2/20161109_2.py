# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        ret = []
        queue.append(root)
        while queue:
            current = queue.pop()
            if not current:
                break
            else:
                ret.append(current.val)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return ret
