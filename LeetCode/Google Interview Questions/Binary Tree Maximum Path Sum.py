# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxGainSum = float('-inf')
        
        def maxGain(node):
            nonlocal maxGainSum
            if node is None:
                return 0
            else:
                leftSubTreeGain = max(0, maxGain(node.left))
                rightSubTreeGain = max(0, maxGain(node.right))
                maxGainSum = max(maxGainSum, node.val + leftSubTreeGain + rightSubTreeGain)
                return node.val + max(leftSubTreeGain, rightSubTreeGain)
        
        maxGain(root)
        return maxGainSum