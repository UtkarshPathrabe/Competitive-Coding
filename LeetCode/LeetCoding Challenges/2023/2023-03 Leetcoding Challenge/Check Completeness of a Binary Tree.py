# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes, i = [(root, 1)], 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, v * 2))
                nodes.append((node.right, v * 2 + 1))
        return nodes[-1][1] == len(nodes)