# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        levelQueue, sign, isEven = [root], 1, 1
        while levelQueue:
            nodeValues = [node.val for node in levelQueue]
            if any(val % 2 != isEven for val in nodeValues) or any(sign * (val2 - val1) <= 0 for val1, val2 in zip(nodeValues, nodeValues[1:])):
                return False
            sign, isEven, levelQueue = sign * -1, isEven ^ 1, [child for node in levelQueue for child in (node.left, node.right) if child]
        return True