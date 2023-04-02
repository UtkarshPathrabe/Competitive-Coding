# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.result = 0
        def helper(node):
            if node is None:
                return 0
            depth = max(helper(node.left), helper(node.right)) + 1
            self.result = max(self.result, depth)
            return depth
        helper(root)
        return self.result