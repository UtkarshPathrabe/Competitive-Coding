# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.result, minValue = float('inf'), root.val
        def dfs(node):
            if node:
                if minValue < node.val < self.result:
                    self.result = node.val
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.result if self.result < float('inf') else -1