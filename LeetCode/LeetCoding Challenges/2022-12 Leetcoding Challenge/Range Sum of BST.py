# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, result = [root,], 0
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    result += node.val
                if node.val <= high and node.right:
                    stack.append(node.right)
                if low <= node.val and node.left:
                    stack.append(node.left)
        return result