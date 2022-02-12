"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def processChildNode(childNode, prev, leftmost):
            if childNode:
                if prev:
                    prev.next = childNode
                else:
                    leftmost = childNode
                prev = childNode
            return prev, leftmost
        if root is None:
            return root
        leftmost = root
        while leftmost:
            curr, prev = leftmost, None
            leftmost = None
            while curr:
                prev, leftmost = processChildNode(curr.left, prev, leftmost)
                prev, leftmost = processChildNode(curr.right, prev, leftmost)
                curr = curr.next
        return root