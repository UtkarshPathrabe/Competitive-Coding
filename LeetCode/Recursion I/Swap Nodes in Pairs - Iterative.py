# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        prevNode = dummyHead
        currentNode = dummyHead.next
        while currentNode and currentNode.next:
            firstNode = currentNode
            secondNode = currentNode.next
            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            prevNode = firstNode
            currentNode = firstNode.next
        return dummyHead.next