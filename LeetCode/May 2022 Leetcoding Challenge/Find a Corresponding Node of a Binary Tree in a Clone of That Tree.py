# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        answer = None
        def inorderTraversal(originalNode, clonedNode):
            nonlocal answer
            if originalNode and answer is None:
                inorderTraversal(originalNode.left, clonedNode.left)
                if originalNode is target:
                    answer = clonedNode
                inorderTraversal(originalNode.right, clonedNode.right)
        inorderTraversal(original, cloned)
        return answer