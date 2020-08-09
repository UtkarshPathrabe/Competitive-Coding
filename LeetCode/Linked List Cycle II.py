# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        def getIntersection(head: ListNode) -> ListNode:
            tortoise = head
            hare = head
            while hare is not None and hare.next is not None:
                tortoise = tortoise.next
                hare = hare.next.next
                if hare == tortoise:
                    return tortoise
            return None
        
        intersection = getIntersection(head)
        if intersection is None:
            return None
        pointer1 = head
        pointer2 = intersection
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1