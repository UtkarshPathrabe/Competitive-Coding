"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        currentNode = head
        while currentNode:
            newNode = Node(currentNode.val, None, None)
            newNode.next = currentNode.next
            currentNode.next = newNode
            currentNode = newNode.next
        currentNode = head
        while currentNode:
            currentNode.next.random = currentNode.random.next if currentNode.random else None
            currentNode = currentNode.next.next
        oldList = head
        newList = head.next
        currentNode = head.next
        while oldList:
            oldList.next = oldList.next.next
            newList.next = newList.next.next if newList.next else None
            oldList = oldList.next
            newList = newList.next
        return currentNode