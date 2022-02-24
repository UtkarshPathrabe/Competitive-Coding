# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        prefixSums = []
        def dfs(node):
            if node is None:
                return 0
            currentSum = dfs(node.left) + dfs(node.right) + node.val
            prefixSums.append(currentSum)
            return currentSum
        result, totalSum = float('-inf'), dfs(root)
        for s in prefixSums:
            result = max(result, s * (totalSum - s))
        return result % (10**9 + 7)