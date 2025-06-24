# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0

        def dfs(node, max_val):
            nonlocal good_count
            if not node:
                return
            if node.val >= max_val:
                good_count += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs(root, root.val)
        return good_count


root = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(1)
node5 = TreeNode(5)

root.left = node1
node1.left = node3
root.right = node2
node2.left = node4
node2.right = node5

print(Solution().goodNodes(root))
