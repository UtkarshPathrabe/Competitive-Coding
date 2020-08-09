# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slowPointer = head
        fastPointer = head.next
        while slowPointer != fastPointer:
            if fastPointer is None or fastPointer.next is None:
                return False
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        return True