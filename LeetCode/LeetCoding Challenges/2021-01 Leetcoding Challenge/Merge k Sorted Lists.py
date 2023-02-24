# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        head = currentNode = ListNode(0)
        priorityQueue = PriorityQueue()
        for linkedList in lists:
            if linkedList:
                priorityQueue.put(Wrapper(linkedList))
        while not priorityQueue.empty():
            node = priorityQueue.get().node
            currentNode.next = node
            currentNode = currentNode.next
            node = node.next
            if node:
                priorityQueue.put(Wrapper(node))
        return head.next