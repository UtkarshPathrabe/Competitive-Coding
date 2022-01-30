# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def constructTree(currentIndex):
            if currentIndex >= len(s):
                return (currentIndex, None)
            if s[currentIndex] == ')':
                return (currentIndex + 1, None)
            currentValue = []
            while currentIndex < len(s) and s[currentIndex] not in ['(', ')']:
                currentValue.append(s[currentIndex])
                currentIndex += 1
            node = TreeNode(int(''.join(currentValue)))
            if currentIndex >= len(s) or s[currentIndex] == ')':
                return (currentIndex + 1, node)
            if currentIndex < len(s) and s[currentIndex] == '(':
                currentIndex, node.left = constructTree(currentIndex + 1)
            if currentIndex < len(s) and s[currentIndex] == '(':
                currentIndex, node.right = constructTree(currentIndex + 1)
            return (currentIndex + 1, node)
        return constructTree(0)[1]