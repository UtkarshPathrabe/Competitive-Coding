"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        rootVal = 0
        for node in tree:
            if node:
                rootVal ^= node.val
                for child in node.children:
                    if child:
                        rootVal ^= child.val
        for node in tree:
            if rootVal == node.val:
                return node
        return None