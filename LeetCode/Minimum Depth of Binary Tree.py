# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        children = [root.left, root.right]
        if not any(children):
            return 1
        minDepth = float('inf')
        for c in children:
            if c:
                minDepth = min(self.minDepth(c), minDepth)
        return minDepth + 1