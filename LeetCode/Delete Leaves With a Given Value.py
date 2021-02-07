# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def isLeaf(node):
            return node.left is None and node.right is None
        def helper(node):
            if isLeaf(node):
                if node.val == target:
                    return None
                else:
                    return node
            else:
                if node.left:
                    node.left = helper(node.left)
                if node.right:
                    node.right = helper(node.right)
                if isLeaf(node) and node.val == target:
                    return None
                return node
        if root is None:
            return root
        return helper(root)
            