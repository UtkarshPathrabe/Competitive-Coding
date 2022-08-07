# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tempArray = []
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                tempArray.append(node.val)
                inorder(node.right)
        inorder(root)
        def constructTree(l: int, r: int):
            if l < r:
                m = l + ((r - l) >> 1)
                return TreeNode(tempArray[m], constructTree(l, m), constructTree(m + 1, r))
            return None
        return constructTree(0, len(tempArray))