# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        nonNineNode = sentinel
        while head:
            if head.val != 9:
                nonNineNode = head
            head = head.next
        nonNineNode.val = nonNineNode.val + 1
        nonNineNode = nonNineNode.next
        while nonNineNode:
            nonNineNode.val = 0
            nonNineNode = nonNineNode.next
        return sentinel if sentinel.val else sentinel.next