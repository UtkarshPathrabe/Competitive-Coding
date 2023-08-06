# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLength, frontNode, endNode, currentNode = 0, None, None, head
        while currentNode != None:
            listLength += 1
            if endNode != None:
                endNode = endNode.next
            if listLength == k:
                frontNode = currentNode
                endNode = head
            currentNode = currentNode.next
        frontNode.val, endNode.val = endNode.val, frontNode.val
        return head