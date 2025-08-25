from typing import Optional, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        def check(root, subRoot):
            if not (root or subRoot):
                return True
            if root == None or subRoot == None or root.val != subRoot.val:
                return False
            return check(root.left, subRoot.left) and check(root.right, subRoot.right)

        if check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
