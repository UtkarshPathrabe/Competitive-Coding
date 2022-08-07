# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def postorder(node: Optional[TreeNode]):
            if not node:
                return 0, float('inf'), float('-inf')
            left_sum, left_min, left_max = postorder(node.left)
            right_sum, right_min, right_max = postorder(node.right)
            if left_max < node.val < right_min:
                total = node.val + left_sum + right_sum
                self.result = max(total, self.result)
                return total, min(left_min, node.val), max(right_max, node.val)
            return 0, float('-inf'), float('inf')
        postorder(root)
        return self.result