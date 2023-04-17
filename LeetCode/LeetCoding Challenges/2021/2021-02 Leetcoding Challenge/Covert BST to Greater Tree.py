# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        currentSum = 0
        def dfs(node):
            nonlocal currentSum
            if node:
                dfs(node.right)
                currentSum += node.val
                node.val = currentSum
                dfs(node.left)
        dfs(root)
        return root