# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node is None:
                return node
            node.left = helper(node.left)
            node.right = helper(node.right)
            return None if node.left is None and node.right is None and node.val == 0 else node
        return helper(root)