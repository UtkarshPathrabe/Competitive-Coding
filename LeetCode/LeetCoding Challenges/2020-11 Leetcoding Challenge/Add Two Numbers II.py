# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        carry, head = 0, None
        while l1 or l2:
            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0
            currentSum = carry + x1 + x2
            val = currentSum % 10
            carry = currentSum // 10
            currNode = ListNode(val)
            currNode.next = head
            head = currNode
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry:
            currNode = ListNode(carry)
            currNode.next = head
            head = currNode
        return head