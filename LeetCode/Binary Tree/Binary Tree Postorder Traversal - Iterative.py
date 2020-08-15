# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, result, node = deque(), [], root
        while stack or node:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            node = stack.pop()
            if stack and stack[-1] == node.right:
                stack[-1] = node
                node = node.right
            else:
                result.append(node.val)
                node = None
        return result