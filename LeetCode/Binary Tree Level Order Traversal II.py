# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            currentLevelQueue = queue
            currentLevelValues = []
            queue = deque([])
            while currentLevelQueue:
                node = currentLevelQueue.popleft()
                currentLevelValues.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevelValues)
        return result[::-1]