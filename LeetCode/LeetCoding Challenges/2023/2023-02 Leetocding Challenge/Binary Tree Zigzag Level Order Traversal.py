# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root,]
        result = []
        reverse = False
        while stack:
            currentStack = stack[::]
            stack = []
            currentLevel = []
            while currentStack:
                node = currentStack.pop()
                if node:
                    currentLevel.append(node.val)
                    if reverse:
                        stack.append(node.right)
                        stack.append(node.left)
                    else:
                        stack.append(node.left)
                        stack.append(node.right)
            reverse = not reverse
            if currentLevel:
                result.append(currentLevel)
        return result
            