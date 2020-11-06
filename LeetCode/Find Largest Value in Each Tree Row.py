# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        heightCache = defaultdict(lambda : float('-inf'))
        
        def preorder(node, depth):
            if not node:
                return
            heightCache[depth] = max(heightCache[depth], node.val)
            preorder(node.left, depth + 1)
            preorder(node.right, depth + 1)
        
        preorder(root, 0)
        result = []
        for i, val in sorted(heightCache.items()):
            result.append(val)
        return result