# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        currentNode = dummyNode
        leadNode = dummyNode
        while n > -1:
            leadNode = leadNode.next
            n -= 1
        while leadNode:
            currentNode = currentNode.next
            leadNode = leadNode.next
        currentNode.next = currentNode.next.next
        return dummyNode.next