# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, node = [], root
        while node:
            if node.left is None:
                result.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = node
                temp = node
                node = node.left
                temp.left = None
        return result