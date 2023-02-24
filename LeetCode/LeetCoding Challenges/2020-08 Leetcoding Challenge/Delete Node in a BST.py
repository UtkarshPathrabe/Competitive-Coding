# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _successorValue(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val
    
    def _predecessorValue(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.right:
                successorValue = self._successorValue(root)
                root.val = successorValue
                root.right = self.deleteNode(root.right, successorValue)
            else:
                predecessorValue = self._predecessorValue(root)
                root.val = predecessorValue
                root.left = self.deleteNode(root.left, predecessorValue)
        return root