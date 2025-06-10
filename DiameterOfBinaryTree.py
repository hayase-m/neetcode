# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            diameter = max(left_height+right_height, diameter)
            return max(left_height, right_height) + 1

        dfs(root)
        return diameter


node1 = TreeNode(val=1)
node2 = TreeNode(val=2)
node3 = TreeNode(val=3)
node4 = TreeNode(val=4)
node5 = TreeNode(val=5)

node1.left = node2
node2.left = node3
node2.right = node4
node3.left = node5
root = node1

print(Solution().diameterOfBinaryTree(root))
