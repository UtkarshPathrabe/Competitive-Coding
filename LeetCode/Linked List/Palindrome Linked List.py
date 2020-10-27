# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        def reverse(currentNode):
            previousNode = None
            while currentNode is not None:
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode
            return previousNode
        
        def firstHalfEnd(head):
            slow = fast = head
            while fast is not None and fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        firstHalfEndNode = firstHalfEnd(head)
        secondHalfStart = reverse(firstHalfEndNode.next)
        result, firstHalfPointer, secondHalfPointer = True, head, secondHalfStart
        while result and secondHalfPointer is not None:
            if firstHalfPointer.val != secondHalfPointer.val:
                result = False
            firstHalfPointer = firstHalfPointer.next
            secondHalfPointer = secondHalfPointer.next
        firstHalfEndNode.next = reverse(secondHalfStart)
        return result