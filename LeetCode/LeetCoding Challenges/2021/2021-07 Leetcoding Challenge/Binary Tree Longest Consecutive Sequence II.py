# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        maxVal = 0
        def longestPath(root):
            nonlocal maxVal
            if not root:
                return [0, 0]
            inr = dcr = 1
            if root.left:
                left = longestPath(root.left)
                if root.val == root.left.val + 1:
                    dcr = left[1] + 1
                elif root.val == root.left.val - 1:
                    inr = left[0] + 1
            if root.right:
                right = longestPath(root.right)
                if root.val == root.right.val + 1:
                    dcr = max(dcr, right[1] + 1)
                elif root.val == root.right.val - 1:
                    inr = max(inr, right[0] + 1)
            maxVal = max(maxVal, dcr + inr - 1)
            return [inr, dcr]
        longestPath(root)
        return maxVal