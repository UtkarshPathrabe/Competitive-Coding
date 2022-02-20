# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderIndexMap = {value: index for index, value in enumerate(inorder)}
        def buildTreeHelper(inorderLeftIndex, inorderRightIndex):
            nonlocal preorder, inorder, inorderIndexMap
            if inorderLeftIndex > inorderRightIndex:
                return None
            value = preorder[0]
            preorder = preorder[1:]
            root = TreeNode(value)
            inorderIndex = inorderIndexMap[value]
            root.left = buildTreeHelper(inorderLeftIndex, inorderIndex - 1)
            root.right = buildTreeHelper(inorderIndex + 1, inorderRightIndex)
            return root
        return buildTreeHelper(0, len(inorder) - 1)