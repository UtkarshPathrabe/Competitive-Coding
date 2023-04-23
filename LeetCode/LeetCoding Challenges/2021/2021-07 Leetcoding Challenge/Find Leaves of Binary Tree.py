# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        def helper(node, tempResult):
            if node is None:
                return (node, tempResult)
            if node.left is None and node.right is None:
                tempResult.append(node.val)
                return (None, tempResult)
            if node.left is not None:
                node.left, tempResult = helper(node.left, tempResult)
            if node.right is not None:
                node.right, tempResult = helper(node.right, tempResult)
            return (node, tempResult)
        
        while root is not None:
            root, tempResult = helper(root, [])
            result.append(tempResult)
        return result