"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result, previousLayer = [], [root,]
        while previousLayer:
            currentLayer = []
            result.append([])
            for node in previousLayer:
                result[-1].append(node.val)
                currentLayer.extend(node.children)
            previousLayer = currentLayer
        return result