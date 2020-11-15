# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node):
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        height = getHeight(root)
        result = [['' for _ in range((1 << height) - 1)] for _ in range(height)]
        def fill(node, level, left, right):
            if node is None:
                return
            result[level][(left + right) // 2] = str(node.val)
            fill(node.left, level + 1, left, (left + right) // 2)
            fill(node.right, level + 1, (left + right + 1) // 2, right)
        fill(root, 0, 0, len(result[0]))
        return result