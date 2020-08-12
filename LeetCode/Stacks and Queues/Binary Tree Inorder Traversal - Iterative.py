# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = deque()
        result = []
        currentNode = root
        while currentNode is not None or len(stack) != 0:
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            currentNode = stack.pop()
            result.append(currentNode.val)
            currentNode = currentNode.right
        return result