"""
                            Maximum Depth of Binary Tree

Return maximum depth:- how much deep we can go from root to leaf node (trick:- count nodes)

"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



