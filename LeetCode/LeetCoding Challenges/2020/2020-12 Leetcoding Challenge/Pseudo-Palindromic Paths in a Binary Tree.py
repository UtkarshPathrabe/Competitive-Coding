# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        count, stack = 0, deque([(root, 0), ])
        while stack:
            node, path = stack.pop()
            if node is not None:
                path = path ^ (1 << node.val)
                if node.left is None and node.right is None:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        return count