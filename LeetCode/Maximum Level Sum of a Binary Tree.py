# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levelSumMap = defaultdict(int)
        
        def dfs(node, level):
            if node:
                levelSumMap[level] += node.val
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        
        dfs(root, 1)
        levelSum = max(levelSumMap.values())
        for level, s in levelSumMap.items():
            if s == levelSum:
                return level