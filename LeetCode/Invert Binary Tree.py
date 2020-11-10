# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            leftSubTree = self.invertTree(root.left)
            rightSubTree = self.invertTree(root.right)
            root.left = rightSubTree
            root.right = leftSubTree
        return root