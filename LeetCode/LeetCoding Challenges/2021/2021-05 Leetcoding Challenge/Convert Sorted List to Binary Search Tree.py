# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getListLength(head):
            currentNode = head
            length = 0
            while currentNode:
                currentNode = currentNode.next
                length += 1
            return length
        def convertToBST(start, end):
            nonlocal head
            if start > end:
                return None
            mid = (start + end) // 2
            left = convertToBST(start, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convertToBST(mid + 1, end)
            return node
        linkedListSize = getListLength(head)
        return convertToBST(0, linkedListSize - 1)