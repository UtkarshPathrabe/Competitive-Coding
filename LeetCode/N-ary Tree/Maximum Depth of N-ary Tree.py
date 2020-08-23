"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth, stack = 0, deque()
        if root is not None:
            stack.append((1, root))
        while stack:
            currentDepth, node = stack.pop()
            if node is not None:
                depth = max(depth, currentDepth)
                for c in node.children:
                    stack.append((currentDepth + 1, c))
        return depth