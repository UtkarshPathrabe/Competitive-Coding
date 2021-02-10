# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isIdentical(s, t):
            if s is None and t is None:
                return True
            elif s is not None and t is not None:
                return s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
            else:
                return False
        def preorder(node):
            nonlocal t
            if node:
                if node.val == t.val:
                    if isIdentical(node, t):
                        return True
                l = preorder(node.left)
                r = preorder(node.right)
                return l or r
            return t is None
        return preorder(s)