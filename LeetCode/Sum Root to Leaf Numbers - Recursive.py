# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def preOrder(node, currentNumber):
            nonlocal rootToLeafSum
            if node is not None:
                currentNumber = currentNumber * 10 + node.val
                if node.left is None and node.right is None:
                    rootToLeafSum += currentNumber
                else:
                    preOrder(node.left, currentNumber)
                    preOrder(node.right, currentNumber)
        rootToLeafSum = 0
        preOrder(root, 0)
        return rootToLeafSum