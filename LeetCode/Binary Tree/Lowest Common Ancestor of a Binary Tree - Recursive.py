# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurseTree(currentNode):
            nonlocal result
            if currentNode is None:
                return False
            left = recurseTree(currentNode.left)
            right = recurseTree(currentNode.right)
            mid = currentNode == p or currentNode == q
            if left + mid + right >= 2:
                result = currentNode
            return left or mid or right
        result = None
        recurseTree(root)
        return result