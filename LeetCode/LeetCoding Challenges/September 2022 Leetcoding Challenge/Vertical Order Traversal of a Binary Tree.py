# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        columnMap, minColumn, maxColumn, result = defaultdict(list), 0, 0, []
        
        def BFS(root):
            queue = deque([(root, 0, 0)])
            nonlocal columnMap, minColumn, maxColumn
            while queue:
                node, row, col = queue.popleft()
                if node:
                    columnMap[col].append((row, node.val))
                    minColumn, maxColumn = min(minColumn, col), max(maxColumn, col)
                    if node.left:
                        queue.append((node.left, row + 1, col - 1))
                    if node.right:
                        queue.append((node.right, row + 1, col + 1))
        
        BFS(root)
        for i in range(minColumn, maxColumn + 1):
            result.append([val for _, val in sorted(columnMap[i])])
        return result