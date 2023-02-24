"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            while node.parent is not None and node.parent.right == node:
                node = node.parent
            return node.parent