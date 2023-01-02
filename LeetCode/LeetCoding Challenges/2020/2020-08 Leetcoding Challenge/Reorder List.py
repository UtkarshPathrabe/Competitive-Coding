# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next