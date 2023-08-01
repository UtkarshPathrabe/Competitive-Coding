# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[Optional[TreeNode]]:
        self.memo = {0: [], 1: [TreeNode(0)]}
        def recurse(n: int):
            if n not in self.memo:
                result = []
                for x in range(n):
                    y = n - 1 - x
                    for left in recurse(x):
                        for right in recurse(y):
                            result.append(TreeNode(0, left, right))
                self.memo[n] = result
            return self.memo[n]
        recurse(N)
        return self.memo[N]