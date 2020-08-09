# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        carry = 0
        dummyHead = ListNode(0)
        currentNode = dummyHead
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            currentSum = carry + x + y
            carry = currentSum // 10
            currentNode.next = ListNode(currentSum % 10)
            currentNode = currentNode.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            currentNode.next = ListNode(carry)
        return dummyHead.next
        