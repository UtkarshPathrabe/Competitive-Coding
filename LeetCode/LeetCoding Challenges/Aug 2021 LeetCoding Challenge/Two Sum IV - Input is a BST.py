# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hashSet = set()
        
        def find(node):
            if node is None:
                return False
            if k - node.val in hashSet:
                return True
            hashSet.add(node.val)
            return find(node.left) or find(node.right)
        
        return find(root)