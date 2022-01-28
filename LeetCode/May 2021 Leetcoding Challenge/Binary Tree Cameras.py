# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.result, covered = 0, {None}
        def dfs(node, parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (parent is None and node not in covered) or node.left not in covered or node.right not in covered:
                    self.result += 1
                    covered.update({node, parent, node.left, node.right})
        dfs(root)
        return self.result