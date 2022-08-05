# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def getMaxIndex(left: int, right: int) -> int:
            maxIndex = left
            for i in range(left + 1, right):
                if nums[maxIndex] < nums[i]:
                    maxIndex = i
            return maxIndex
        def construct(left: int, right: int) -> Optional[TreeNode]:
            if left == right:
                return None
            maxIndex = getMaxIndex(left, right)
            return TreeNode(nums[maxIndex], construct(left, maxIndex), construct(maxIndex + 1, right))
        return construct(0, len(nums))