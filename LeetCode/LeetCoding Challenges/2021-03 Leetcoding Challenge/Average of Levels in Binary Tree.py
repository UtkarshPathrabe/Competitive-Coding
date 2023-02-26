# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue, levelsData, result = deque([(root, 0)]), defaultdict(lambda : (0, 0)), []
        while queue:
            node, level = queue.popleft()
            if node:
                currentSum, currentCount = levelsData[level]
                currentSum += node.val
                currentCount += 1
                levelsData[level] = (currentSum, currentCount)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        for key in sorted(levelsData.keys()):
            result.append(levelsData[key][0] / levelsData[key][1])
        return result