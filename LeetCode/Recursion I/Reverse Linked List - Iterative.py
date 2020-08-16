# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prevNode = None
        currentNode = head
        while currentNode:
            tempNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = tempNode
        return prevNode