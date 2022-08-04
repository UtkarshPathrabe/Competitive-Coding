# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        def preorder(node: Optional[TreeNode]):
            if node:
                result.append(str(node.val))
                if node.left and node.right:
                    result.append('(')
                    preorder(node.left)
                    result.append(')')
                    result.append('(')
                    preorder(node.right)
                    result.append(')')
                elif node.left:
                    result.append('(')
                    preorder(node.left)
                    result.append(')')
                elif node.right:
                    result.append('(')
                    result.append(')')
                    result.append('(')
                    preorder(node.right)
                    result.append(')')
        preorder(root)
        return ''.join(result)