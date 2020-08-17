# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def computeDepth(node):
            depth = 0
            while node.left:
                node = node.left
                depth += 1
            return depth
        def nodeExists(index, depth, node):
            left, right = 0, 2**depth - 1
            for _ in range(depth):
                pivot = left + ((right - left) // 2)
                if index <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None
        if root is None:
            return 0
        depth = computeDepth(root)
        if depth == 0:
            return 1
        left, right = 1, 2**depth - 1
        while left <= right:
            pivot = left + ((right - left) // 2)
            if nodeExists(pivot, depth, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2**depth - 1) + left