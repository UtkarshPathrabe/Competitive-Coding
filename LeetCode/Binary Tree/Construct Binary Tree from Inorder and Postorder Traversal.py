# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorderIndexMap = {value: index for index, value in enumerate(inorder)}
        def buildTreeHelper(inorderLeftIndex, inorderRightIndex):
            nonlocal inorder, postorder, inorderIndexMap
            if inorderLeftIndex > inorderRightIndex:
                return None
            value = postorder.pop()
            root = TreeNode(value)
            inorderIndex = inorderIndexMap[value]
            root.right = buildTreeHelper(inorderIndex + 1, inorderRightIndex)
            root.left = buildTreeHelper(inorderLeftIndex, inorderIndex - 1)
            return root
        return buildTreeHelper(0, len(inorder) - 1)