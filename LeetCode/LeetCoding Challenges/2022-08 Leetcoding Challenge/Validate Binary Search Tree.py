# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = deque(), float('-inf')
        currentNode = root
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            currentNode = stack.pop()
            if currentNode.val <= inorder:
                return False
            inorder = currentNode.val
            currentNode = currentNode.right
        return True