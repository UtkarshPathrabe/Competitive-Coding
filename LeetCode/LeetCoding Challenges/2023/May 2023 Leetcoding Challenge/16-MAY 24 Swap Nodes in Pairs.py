# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        newHead = prev
        temp = head
        while temp and temp.next:
            nextSetNode = temp.next.next
            currSetHead = temp.next
            temp.next.next = temp
            temp.next = nextSetNode
            temp = nextSetNode
            prev.next = currSetHead
            prev = prev.next.next
        return newHead.next