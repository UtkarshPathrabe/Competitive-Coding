# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None
        current, prev = head, None
        while left > 1:
            prev = current
            current = current.next
            left, right = left - 1, right - 1
        tail, con = current, prev
        while right:
            third = current.next
            current.next = prev
            prev = current
            current = third
            right -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = current
        return head