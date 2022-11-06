# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        def insert(node: Optional[TreeNode], currentDepth: int):
            if node is None:
                return
            if currentDepth == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            else:
                insert(node.left, currentDepth + 1)
                insert(node.right, currentDepth + 1)
        insert(root, 1)
        return root