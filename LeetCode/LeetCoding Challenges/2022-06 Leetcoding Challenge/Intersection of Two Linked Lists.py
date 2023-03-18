# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA is not None else headB
            pointerB = pointerB.next if pointerB is not None else headA
        return pointerA