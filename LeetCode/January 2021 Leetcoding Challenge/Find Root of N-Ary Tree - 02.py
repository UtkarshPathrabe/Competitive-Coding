"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seenNodes = set()
        for node in tree:
            seenNodes.add(node)
        for node in tree:
            for child in node.children:
                seenNodes.remove(child)
        for node in seenNodes:
            return node
        return None