# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def inorder(node: Optional[TreeNode]):
            if node:
                inorder(node.left)
                freq[node.val] += 1
                inorder(node.right)
        inorder(root)
        maxFreq = max(freq.values())
        return [x[0] for x in freq.items() if x[1] == maxFreq]