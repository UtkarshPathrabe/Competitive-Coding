# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longestPath = 0
        
        def longestArrow(node):
            nonlocal longestPath
            if node is None:
                return 0
            else:
                leftLength = longestArrow(node.left)
                rightLength = longestArrow(node.right)
                leftArrowLength = rightArrowLength = 0
                if node.left and node.left.val == node.val:
                    leftArrowLength = leftLength + 1
                if node.right and node.right.val == node.val:
                    rightArrowLength = rightLength + 1
                longestPath = max(longestPath, leftArrowLength + rightArrowLength)
                return max(leftArrowLength, rightArrowLength)
        
        longestArrow(root)
        return longestPath