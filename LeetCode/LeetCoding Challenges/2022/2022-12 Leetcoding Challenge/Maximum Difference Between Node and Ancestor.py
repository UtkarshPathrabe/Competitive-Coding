# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        def getDiff(node, maxVal, minVal):
            if node is None:
                return abs(maxVal - minVal)
            maxVal = max(maxVal, node.val)
            minVal = min(minVal, node.val)
            left = getDiff(node.left, maxVal, minVal)
            right = getDiff(node.right, maxVal, minVal)
            return max(left, right)
        return getDiff(root, root.val, root.val)