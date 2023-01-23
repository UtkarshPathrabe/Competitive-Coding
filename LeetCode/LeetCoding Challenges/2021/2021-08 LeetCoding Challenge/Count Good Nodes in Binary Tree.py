# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            for child in filter(None, [node.left, node.right]):
                count += child.val >= node.val
                child.val = max(child.val, node.val)
                dfs(child)
        dfs(root)
        return count + 1