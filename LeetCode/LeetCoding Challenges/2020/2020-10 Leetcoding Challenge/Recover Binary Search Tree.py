# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, x, y, predecessor = deque(), None, None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if predecessor and root.val < predecessor.val:
                y = root
                if x is None:
                    x = predecessor
                else:
                    break
            predecessor = root
            root = root.right
        x.val, y.val = y.val, x.val