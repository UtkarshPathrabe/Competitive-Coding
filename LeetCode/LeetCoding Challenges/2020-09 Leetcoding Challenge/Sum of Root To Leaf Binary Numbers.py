# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0
        
        def sumPath(node, binaryString):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.sum += int(binaryString + str(node.val), base=2)
                return
            if node.left:
                sumPath(node.left, binaryString + str(node.val))
            if node.right:
                sumPath(node.right, binaryString + str(node.val))
        
        sumPath(root, '')
        return self.sum