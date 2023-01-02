# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        result = 0
        
        def getSum(node):
            nonlocal result
            if node is None:
                return 0
            leftSum = getSum(node.left)
            rightSum = getSum(node.right)
            result += abs(rightSum - leftSum)
            return leftSum + rightSum + node.val
        
        getSum(root)
        return result