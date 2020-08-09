# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        def mergeTwoLists(l1, l2):
            head = current = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1 is None:
                current.next = l2
            else:
                current.next = l1
            return head.next
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount-interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists