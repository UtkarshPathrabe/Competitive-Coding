# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalancedHelper(node):
            if node is None:
                return 0
            leftSubtree = isBalancedHelper(node.left)
            rightSubtree = isBalancedHelper(node.right)
            if (leftSubtree == -1 or rightSubtree == -1 or abs(leftSubtree - rightSubtree) > 1):
                return -1
            return max(leftSubtree, rightSubtree) + 1
        return isBalancedHelper(root) != -1