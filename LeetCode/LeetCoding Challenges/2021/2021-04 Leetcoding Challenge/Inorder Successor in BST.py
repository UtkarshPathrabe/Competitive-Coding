# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            stack, inorderPrev, currentNode = deque(), float('-inf'), root
            while currentNode or stack:
                while currentNode:
                    stack.append(currentNode)
                    currentNode = currentNode.left
                currentNode = stack.pop()
                if inorderPrev == p.val:
                    return currentNode
                inorderPrev = currentNode.val
                currentNode = currentNode.right
        return None