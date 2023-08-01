# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        result, prev = float('inf'), float('-inf')
        def inorder(node):
            nonlocal result, prev
            if node:
                inorder(node.left)
                result = min(result, node.val - prev)
                prev = node.val
                inorder(node.right)
        inorder(root)
        return result