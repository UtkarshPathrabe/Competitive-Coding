# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        stack = deque([(root, 0)])
        while stack:
            node, currentSum = stack.pop()
            if node is not None:
                currentSum += node.val
                if node.left is None and node.right is None:
                    if currentSum == s:
                        return True
                else:
                    stack.append((node.left, currentSum))
                    stack.append((node.right, currentSum))
        return False