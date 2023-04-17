# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyNode = ListNode('D')
        currentNode = dummyNode
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                currentNode.next = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next
            if currentNode and currentNode.next:
                currentNode = currentNode.next
        if l1 is None and l2 is not None:
            currentNode.next = l2
        elif l1 is not None and l2 is None:
            currentNode.next = l1
        else:
            currentNode.next = None
        return dummyNode.next