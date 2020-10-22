# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.result = float('inf')
        def calculateDepth(node, depth):
            if node:
                if node.left is None and node.right is None:
                    self.result = min(self.result, depth + 1)
                else:
                    if node.left:
                        calculateDepth(node.left, depth + 1)
                    if node.right:
                        calculateDepth(node.right, depth + 1)
        calculateDepth(root, 0)
        return 0 if self.result == float('inf') else self.result