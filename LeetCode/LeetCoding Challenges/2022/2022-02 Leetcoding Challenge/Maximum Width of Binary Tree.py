# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue, result = deque([(0, root), ]), 0
        while queue:
            n, nodes = len(queue), []
            for _ in range(n):
                index, node = queue.popleft()
                nodes.append(index)
                if node.left:
                    queue.append((2 * index + 1, node.left))
                if node.right:
                    queue.append((2 * index + 2, node.right))
            result = max(result, max(nodes) - min(nodes) + 1)
        return result
                