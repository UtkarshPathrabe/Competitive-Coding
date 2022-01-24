# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(start, end):
            if start > end:
                return None
            else:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = helper(start, mid - 1)
                node.right = helper(mid + 1, end)
                return node
        return helper(0, len(nums) - 1)