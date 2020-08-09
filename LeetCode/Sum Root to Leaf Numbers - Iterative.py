# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        rootToLeafSum = 0
        stack = [(root, 0)]
        while len(stack) != 0:
            node, currentNumber = stack.pop()
            if node is not None:
                currentNumber = currentNumber * 10 + node.val
                if node.left is None and node.right is None:
                    rootToLeafSum += currentNumber
                else:
                    stack.append((node.left, currentNumber))
                    stack.append((node.right, currentNumber))
        return rootToLeafSum