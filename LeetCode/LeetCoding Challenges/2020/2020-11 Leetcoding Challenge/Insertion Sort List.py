# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(float('-inf'), head)
        currentNode = dummyHead.next
        while currentNode and currentNode.next:
            if currentNode.val <= currentNode.next.val:
                currentNode = currentNode.next
            else:
                tempNode = currentNode.next
                currentNode.next = tempNode.next
                iterator = dummyHead
                while iterator.next and iterator.next.val <= tempNode.val:
                    iterator = iterator.next
                tempNode.next = iterator.next
                iterator.next = tempNode
        return dummyHead.next