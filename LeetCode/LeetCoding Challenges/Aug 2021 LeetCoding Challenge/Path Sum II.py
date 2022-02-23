# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        stack = deque([(root, 0, [])])
        result = []
        while stack:
            node, currentSum, currentPath = stack.pop()
            if node is not None:
                currentSum += node.val
                currentPath.append(node.val)
                if node.left is None and node.right is None:
                    if currentSum == s:
                        result.append(list(currentPath))
                else:
                    if node.left:
                        stack.append((node.left, currentSum, list(currentPath)))
                    if node.right:
                        stack.append((node.right, currentSum, list(currentPath)))
        return result