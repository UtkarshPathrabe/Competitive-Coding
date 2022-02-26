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
        if root is None:
            return root
        queue = [root]
        while queue:
            nextLevelQueue = []
            prev = queue[0]
            if prev.left:
                nextLevelQueue.append(prev.left)
            if prev.right:
                nextLevelQueue.append(prev.right)
            for i in range(1, len(queue)):
                node = queue[i]
                prev.next = node
                prev = node
                if node.left:
                    nextLevelQueue.append(node.left)
                if node.right:
                    nextLevelQueue.append(node.right)
            queue = nextLevelQueue
        return root