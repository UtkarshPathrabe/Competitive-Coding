# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def constructBST(l: int, r: int) -> Optional[TreeNode]:
            if l >= r:
                return None
            splitIndex = l + 1
            while splitIndex < r and preorder[splitIndex] < preorder[l]:
                splitIndex += 1
            return TreeNode(preorder[l], constructBST(l + 1, splitIndex), constructBST(splitIndex, r))
        return constructBST(0, len(preorder))