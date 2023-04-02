# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        count = 0
        sumMap = defaultdict(int)
        def preOrderTraversal(node, currentSum):
            nonlocal count, sumMap, s
            if node is not None:
                currentSum += node.val
                if currentSum == s:
                    count += 1
                count += sumMap[currentSum - s]
                sumMap[currentSum] += 1
                preOrderTraversal(node.left, currentSum)
                preOrderTraversal(node.right, currentSum)
                sumMap[currentSum] -= 1
        preOrderTraversal(root, 0)
        return count