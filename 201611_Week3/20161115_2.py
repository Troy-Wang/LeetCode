"""
Kth smalllest in a BST
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        current = root
        count = 0
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            if stack:
                current = stack.pop()
                count += 1
                if count == k:
                    return current.val
                current = current.right
