# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = '~'
        def dfs(node: Optional[TreeNode], currentChars):
            if node:
                currentChars.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.result = min(self.result, ''.join(reversed(currentChars)))
                else:
                    dfs(node.left, currentChars)
                    dfs(node.right, currentChars)
                currentChars.pop()
        dfs(root, [])
        return self.result