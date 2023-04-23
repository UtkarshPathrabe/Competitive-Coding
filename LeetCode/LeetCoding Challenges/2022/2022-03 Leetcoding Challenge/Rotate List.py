# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        getHeadIndex = lambda k, listLength : (listLength - k) % listLength
        getTailIndex = lambda newHeadIndex, listLength : (newHeadIndex - 1) % listLength
        listLength, currentNode = 1, head
        while currentNode.next is not None:
            listLength += 1
            currentNode = currentNode.next
        currentNode.next = head
        headIndex = getHeadIndex(k, listLength)
        tailIndex = getTailIndex(headIndex, listLength)
        currentNode, i = head, 0
        while i < tailIndex:
            currentNode = currentNode.next
            i += 1
        head = currentNode.next
        currentNode.next = None
        return head