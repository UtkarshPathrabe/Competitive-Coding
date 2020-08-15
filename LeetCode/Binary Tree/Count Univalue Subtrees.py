# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        count = 0
        
        def isValid(node, value):
            if node is None:
                return True
            if not all([isValid(node.left, node.val), isValid(node.right, node.val)]):
                return False
            nonlocal count
            count += 1
            return node.val == value
        
        isValid(root, 0)
        return count