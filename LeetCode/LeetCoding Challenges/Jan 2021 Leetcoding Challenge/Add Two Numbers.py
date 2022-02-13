# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2, carry, currentSum, dummyHead = 0, 0, 0, 0, ListNode(0)
        currentNode = dummyHead
        while l1 is not None or l2 is not None:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            currentSum = num1 + num2 + carry
            currentNode.next = ListNode(currentSum % 10)
            currentNode = currentNode.next
            carry = currentSum // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry:
            currentNode.next = ListNode(carry)
        return dummyHead.next