# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 1
        
        def depthOfTree(node):
            nonlocal diameter
            if node is None:
                return 0
            else:
                leftTreeDepth = depthOfTree(node.left)
                rightTreeDepth = depthOfTree(node.right)
                diameter = max(diameter, 1 + leftTreeDepth + rightTreeDepth)
                return 1 + max(leftTreeDepth, rightTreeDepth)
        
        depthOfTree(root)
        return diameter - 1