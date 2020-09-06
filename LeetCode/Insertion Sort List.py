# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(float('-inf'))
        dummyHead.next = head
        current = dummyHead.next
        while current and current.next:
            if current.val <= current.next.val:
                current = current.next
            else:
                temp = current.next
                current.next = temp.next
                iterator = dummyHead
                while iterator.next and iterator.next.val <= temp.val:
                    iterator = iterator.next
                temp.next = iterator.next
                iterator.next = temp
        return dummyHead.next