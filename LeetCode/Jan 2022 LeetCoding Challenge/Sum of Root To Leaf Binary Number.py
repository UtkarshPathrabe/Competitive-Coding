# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preOrder(node, currentSum):
            nonlocal rootToLeafSum
            if node:
                currentSum = currentSum * 2 + node.val
                if node.left is None and node.right is None:
                    rootToLeafSum += currentSum
                else:
                    preOrder(node.left, currentSum)
                    preOrder(node.right, currentSum)
        rootToLeafSum = 0
        preOrder(root, 0)
        return rootToLeafSum