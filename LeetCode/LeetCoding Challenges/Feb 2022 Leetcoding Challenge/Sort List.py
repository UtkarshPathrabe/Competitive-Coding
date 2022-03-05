# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMiddleNode(node):
            slow = fast = node
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergeLists(nodeA, nodeB):
            if nodeA is None:
                return nodeB
            if nodeB is None:
                return nodeA
            newList = None
            if nodeA.val <= nodeB.val:
                newList = nodeA
                newList.next = mergeLists(nodeA.next, nodeB)
            else:
                newList = nodeB
                newList.next = mergeLists(nodeA, nodeB.next)
            return newList
        
        def mergeSort(node):
            if node is None or node.next is None:
                return node
            middleNode = getMiddleNode(node)
            middleNodeNext = middleNode.next
            middleNode.next = None
            leftList = mergeSort(node)
            rightList = mergeSort(middleNodeNext)
            return mergeLists(leftList, rightList)
        
        return mergeSort(head)