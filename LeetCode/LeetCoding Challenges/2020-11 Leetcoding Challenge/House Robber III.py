# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            rob = node.val + left[1] + right[1]
            notRob = max(left) + max(right)
            return (rob, notRob)
        return max(helper(root))