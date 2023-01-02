# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
        return TreeNode(val)